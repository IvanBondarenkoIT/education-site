#!/usr/bin/env python
"""
Скрипт для извлечения контента из fixtures в Markdown-файлы.
Запуск: python scripts/extract_content_to_md.py
Выход: content/ (создаётся в корне проекта)
"""
import json
import os
import re
from pathlib import Path

# Category display names
BV_CATEGORIES = {
    'competence': 'Компетентность',
    'leadership': 'Лидерство',
    'uniqueness': 'Уникальность',
    'team': 'Команда',
    'espresso_culture': 'Эспрессо культура',
}


def clean_text(text):
    """Убирает лишние переносы и табуляции из текста."""
    if not text:
        return ''
    return re.sub(r'[\n\t]+', ' ', text).strip()


def strip_html(html):
    """Упрощённое удаление HTML-тегов."""
    if not html:
        return ''
    text = re.sub(r'<[^>]+>', ' ', html)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


def format_training_content(text):
    """Форматирует контент обучения: 1. 2. -> заголовки, • -> списки."""
    if not text:
        return ''
    # Split by numbered items like "1." "2." "3."
    parts = re.split(r'(\d+\.)', text)
    result = []
    for i, p in enumerate(parts):
        p = p.strip()
        if not p:
            continue
        if re.match(r'^\d+\.$', p):
            continue  # Skip standalone number
        # Split by bullet •
        if '•' in p:
            lines = [x.strip() for x in p.split('•') if x.strip()]
            for line in lines:
                if line:
                    result.append(f'- {line}')
        else:
            result.append(p)
    return '\n\n'.join(result) if result else text


def main():
    base = Path(__file__).resolve().parent.parent
    fixtures_path = base / 'core' / 'fixtures' / 'all_data.json'
    content_dir = base / 'content'

    with open(fixtures_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    content_dir.mkdir(exist_ok=True)

    # Group by model
    bv_items = []
    tp_items = []
    ji_items = []
    ci_items = []

    for item in data:
        model = item.get('model', '')
        if 'businessvalue' in model:
            bv_items.append(item)
        elif 'trainingprogram' in model:
            tp_items.append(item)
        elif 'jobinstruction' in model:
            ji_items.append(item)
        elif 'coffeeinfo' in model:
            ci_items.append(item)

    # --- Business Values ---
    bv_by_cat = {}
    for item in bv_items:
        f = item['fields']
        cat = f.get('category', 'other')
        if cat not in bv_by_cat:
            bv_by_cat[cat] = []
        situation = clean_text(f.get('situation_ru') or f.get('situation', ''))
        value = clean_text(f.get('business_value_ru') or f.get('business_value', ''))
        bv_by_cat[cat].append((f.get('order', 0), situation, value))

    bv_path = content_dir / 'business_values.md'
    with open(bv_path, 'w', encoding='utf-8') as out:
        out.write('# Бизнес-ценности компании DimKava\n\n')
        out.write('*Источник: core/fixtures/all_data.json (BusinessValue)*\n\n')
        out.write('---\n\n')
        for cat_key in ['competence', 'leadership', 'team', 'uniqueness', 'espresso_culture']:
            if cat_key not in bv_by_cat:
                continue
            cat_name = BV_CATEGORIES.get(cat_key, cat_key)
            out.write(f'## {cat_name}\n\n')
            items = sorted(bv_by_cat[cat_key], key=lambda x: x[0])
            for i, (_, situation, value) in enumerate(items, 1):
                out.write(f'### {i}. {situation}\n\n')
                out.write(f'**Ценность:** {value}\n\n')
            out.write('---\n\n')

    # --- Training Program ---
    tp_path = content_dir / 'training_program.md'
    with open(tp_path, 'w', encoding='utf-8') as out:
        out.write('# Программа обучения сотрудников\n\n')
        out.write('*Источник: core/fixtures/all_data.json (TrainingProgram)*\n\n')
        period_names = {'day': 'День', 'week': 'Неделя', 'month': 'Месяц'}
        for item in sorted(tp_items, key=lambda x: (x['fields'].get('period_type', ''), x['fields'].get('period_number', 0))):
            f = item['fields']
            pt = f.get('period_type', 'day')
            pn = f.get('period_number', 0)
            title = f.get('title_ru') or f.get('title', '')
            content = f.get('content_ru') or f.get('content', '')
            content_clean = format_training_content(strip_html(content))
            out.write(f'## {period_names.get(pt, pt)} {pn}: {title}\n\n')
            out.write(content_clean)
            out.write('\n\n---\n\n')

    # --- Job Instructions ---
    ji_path = content_dir / 'job_instructions.md'
    with open(ji_path, 'w', encoding='utf-8') as out:
        out.write('# Должностные инструкции\n\n')
        out.write('*Источник: core/fixtures/all_data.json (JobInstruction)*\n\n')
        for item in ji_items:
            f = item['fields']
            title = f.get('title_ru') or f.get('title', '')
            content = f.get('content_ru') or f.get('content', '')
            content_clean = strip_html(content)
            out.write(f'## {title}\n\n')
            out.write(f'*Должность: {f.get("position", "")} | Отдел: {f.get("department", "")}*\n\n')
            out.write(content_clean)
            out.write('\n\n---\n\n')

    # --- Coffee Info ---
    ci_path = content_dir / 'coffee_info.md'
    with open(ci_path, 'w', encoding='utf-8') as out:
        out.write('# Информация о кофе\n\n')
        out.write('*Источник: core/fixtures/all_data.json (CoffeeInfo)*\n\n')
        for item in ci_items:
            f = item['fields']
            title = f.get('title_ru') or f.get('title', '')
            content = f.get('content_ru') or f.get('content', '')
            content_clean = strip_html(content)
            out.write(f'## {title}\n\n')
            out.write(f'*Категория: {f.get("category", "")}*\n\n')
            out.write(content_clean)
            out.write('\n\n---\n\n')

    print(f'Extracted to {content_dir}:')
    print(f'  - business_values.md ({len(bv_items)} items)')
    print(f'  - training_program.md ({len(tp_items)} items)')
    print(f'  - job_instructions.md ({len(ji_items)} items)')
    print(f'  - coffee_info.md ({len(ci_items)} items)')


if __name__ == '__main__':
    main()
