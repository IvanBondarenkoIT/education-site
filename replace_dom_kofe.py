#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Скрипт для замены "Дом Кофе" на "Dim Kava" в фикстурах
"""

import json
import os
from pathlib import Path

def replace_in_fixtures():
    """Заменяет 'Дом Кофе' на 'Dim Kava' в фикстурах"""
    fixtures_file = Path('core/fixtures/all_data.json')
    
    if not fixtures_file.exists():
        print(f"Файл {fixtures_file} не найден")
        return
    
    print(f"Загружаем фикстуры из {fixtures_file}...")
    
    # Загружаем данные
    with open(fixtures_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    print(f"Загружено {len(data)} записей")
    
    # Заменяем "Дом Кофе" на "Dim Kava"
    replacements = 0
    for item in data:
        for key, value in item.items():
            if isinstance(value, str) and 'Дом Кофе' in value:
                old_value = value
                new_value = value.replace('Дом Кофе', 'Dim Kava')
                item[key] = new_value
                replacements += 1
                print(f"Заменено в {key}: {old_value[:50]}... -> {new_value[:50]}...")
    
    print(f"Всего замен: {replacements}")
    
    # Сохраняем обновленные данные
    with open(fixtures_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"Фикстуры обновлены: {fixtures_file}")

if __name__ == '__main__':
    replace_in_fixtures()
