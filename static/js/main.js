/**
 * Main JavaScript file for Coffee Education Site
 * Основной JavaScript файл для образовательного сайта кофейни
 */

(function() {
    'use strict';

    // DOM Ready
    document.addEventListener('DOMContentLoaded', function() {
        initializeComponents();
        setupEventListeners();
    });

    /**
     * Initialize all components
     * Инициализация всех компонентов
     */
    function initializeComponents() {
        initializeBackToTop();
        initializeTooltips();
        initializeLanguageSwitcher();
        initializeMobileMenu();
    }

    /**
     * Setup event listeners
     * Настройка обработчиков событий
     */
    function setupEventListeners() {
        // Scroll event for back to top button
        window.addEventListener('scroll', handleScroll);
        
        // Form validation
        setupFormValidation();
        
        // Smooth scrolling for anchor links
        setupSmoothScrolling();
    }

    /**
     * Initialize back to top button
     * Инициализация кнопки "наверх"
     */
    function initializeBackToTop() {
        const backToTopBtn = document.querySelector('.back-to-top');
        if (!backToTopBtn) return;

        backToTopBtn.addEventListener('click', function() {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }

    /**
     * Handle scroll events
     * Обработка событий прокрутки
     */
    function handleScroll() {
        const backToTopBtn = document.querySelector('.back-to-top');
        if (!backToTopBtn) return;

        if (window.pageYOffset > 300) {
            backToTopBtn.classList.add('show');
        } else {
            backToTopBtn.classList.remove('show');
        }
    }

    /**
     * Initialize Bootstrap tooltips
     * Инициализация подсказок Bootstrap
     */
    function initializeTooltips() {
        const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
        tooltipTriggerList.map(function(tooltipTriggerEl) {
            return new bootstrap.Tooltip(tooltipTriggerEl);
        });
    }

    /**
     * Initialize language switcher
     * Инициализация переключателя языков
     */
    function initializeLanguageSwitcher() {
        const languageLinks = document.querySelectorAll('.language-switcher__item');
        
        languageLinks.forEach(function(link) {
            link.addEventListener('click', function(e) {
                // Add loading state
                const button = document.querySelector('.language-switcher__button');
                if (button) {
                    button.innerHTML = '<span class="spinner"></span> Загрузка...';
                    button.disabled = true;
                }
                
                // The actual language change will be handled by Django
                // Фактическое изменение языка будет обработано Django
            });
        });
    }

    /**
     * Initialize mobile menu
     * Инициализация мобильного меню
     */
    function initializeMobileMenu() {
        const navbarToggler = document.querySelector('.navbar-toggler');
        const navbarCollapse = document.querySelector('.navbar-collapse');
        
        if (!navbarToggler || !navbarCollapse) return;

        // Close mobile menu when clicking on a link
        const navLinks = navbarCollapse.querySelectorAll('.nav-link');
        navLinks.forEach(function(link) {
            link.addEventListener('click', function() {
                if (window.innerWidth < 992) {
                    const bsCollapse = new bootstrap.Collapse(navbarCollapse);
                    bsCollapse.hide();
                }
            });
        });

        // Close mobile menu when clicking outside
        document.addEventListener('click', function(e) {
            if (!navbarCollapse.contains(e.target) && !navbarToggler.contains(e.target)) {
                if (navbarCollapse.classList.contains('show')) {
                    const bsCollapse = new bootstrap.Collapse(navbarCollapse);
                    bsCollapse.hide();
                }
            }
        });
    }

    /**
     * Setup form validation
     * Настройка валидации форм
     */
    function setupFormValidation() {
        const forms = document.querySelectorAll('.needs-validation');
        
        forms.forEach(function(form) {
            form.addEventListener('submit', function(e) {
                if (!form.checkValidity()) {
                    e.preventDefault();
                    e.stopPropagation();
                }
                
                form.classList.add('was-validated');
            });
        });
    }

    /**
     * Setup smooth scrolling for anchor links
     * Настройка плавной прокрутки для якорных ссылок
     */
    function setupSmoothScrolling() {
        const anchorLinks = document.querySelectorAll('a[href^="#"]');
        
        anchorLinks.forEach(function(link) {
            link.addEventListener('click', function(e) {
                const href = this.getAttribute('href');
                
                if (href === '#') return;
                
                const target = document.querySelector(href);
                if (target) {
                    e.preventDefault();
                    
                    const offsetTop = target.offsetTop - 80; // Account for fixed header
                    
                    window.scrollTo({
                        top: offsetTop,
                        behavior: 'smooth'
                    });
                }
            });
        });
    }

    /**
     * Utility function to show loading state
     * Утилитарная функция для показа состояния загрузки
     */
    window.showLoading = function(element) {
        if (element) {
            element.disabled = true;
            element.innerHTML = '<span class="spinner"></span> Загрузка...';
        }
    };

    /**
     * Utility function to hide loading state
     * Утилитарная функция для скрытия состояния загрузки
     */
    window.hideLoading = function(element, originalText) {
        if (element) {
            element.disabled = false;
            element.innerHTML = originalText || 'Отправить';
        }
    };

    /**
     * Utility function to show alert
     * Утилитарная функция для показа уведомлений
     */
    window.showAlert = function(message, type = 'info') {
        const alertContainer = document.getElementById('alert-container');
        if (!alertContainer) return;

        const alertHtml = `
            <div class="alert alert-${type} alert-dismissible fade show" role="alert">
                ${message}
                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
            </div>
        `;
        
        alertContainer.innerHTML = alertHtml;
        
        // Auto dismiss after 5 seconds
        setTimeout(function() {
            const alert = alertContainer.querySelector('.alert');
            if (alert) {
                const bsAlert = new bootstrap.Alert(alert);
                bsAlert.close();
            }
        }, 5000);
    };

    /**
     * Utility function to format dates
     * Утилитарная функция для форматирования дат
     */
    window.formatDate = function(dateString) {
        const date = new Date(dateString);
        return date.toLocaleDateString('ru-RU', {
            year: 'numeric',
            month: 'long',
            day: 'numeric'
        });
    };

    /**
     * Utility function to truncate text
     * Утилитарная функция для обрезки текста
     */
    window.truncateText = function(text, maxLength = 100) {
        if (text.length <= maxLength) return text;
        return text.substring(0, maxLength) + '...';
    };

})();
