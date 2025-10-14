// Smooth scrolling for navigation links
document.addEventListener('DOMContentLoaded', function() {
    // Get all navigation links
    const navLinks = document.querySelectorAll('.nav-link');
    
    // Add click event listener to each navigation link
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            
            // Remove active class from all links
            navLinks.forEach(l => l.classList.remove('active'));
            
            // Add active class to clicked link
            this.classList.add('active');
            
            // Get the target section
            const targetId = this.getAttribute('href');
            const targetSection = document.querySelector(targetId);
            
            if (targetSection) {
                // Calculate offset for fixed header
                const headerHeight = document.querySelector('.header').offsetHeight;
                const targetPosition = targetSection.offsetTop - headerHeight - 20;
                
                // Smooth scroll to target
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
    
    // Update active navigation link on scroll
    window.addEventListener('scroll', function() {
        const sections = document.querySelectorAll('section[id]');
        const scrollPos = window.scrollY + document.querySelector('.header').offsetHeight + 50;
        
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.offsetHeight;
            const sectionId = section.getAttribute('id');
            
            if (scrollPos >= sectionTop && scrollPos < sectionTop + sectionHeight) {
                navLinks.forEach(link => {
                    link.classList.remove('active');
                    if (link.getAttribute('href') === `#${sectionId}`) {
                        link.classList.add('active');
                    }
                });
            }
        });
    });
    
    // Animate research cards on scroll
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);
    
    // Observe research cards, publication items, and news items
    const animatedElements = document.querySelectorAll('.research-card, .publication-item, .news-item, .person-card');
    animatedElements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(el);
    });
    
    // Add delay for staggered animation
    animatedElements.forEach((el, index) => {
        el.style.transitionDelay = `${index * 0.1}s`;
    });
    
    // Mobile navigation toggle (for future enhancement)
    const createMobileMenu = () => {
        const header = document.querySelector('.header');
        const nav = document.querySelector('.navigation');
        
        // Create hamburger button
        const hamburger = document.createElement('button');
        hamburger.className = 'hamburger';
        hamburger.innerHTML = '☰';
        hamburger.style.display = 'none';
        hamburger.style.background = 'none';
        hamburger.style.border = 'none';
        hamburger.style.fontSize = '1.5rem';
        hamburger.style.cursor = 'pointer';
        hamburger.style.color = '#2c3e50';
        
        // Insert hamburger button
        header.querySelector('.container').appendChild(hamburger);
        
        // Toggle mobile menu
        hamburger.addEventListener('click', () => {
            nav.classList.toggle('mobile-active');
        });
        
        // Show/hide hamburger based on screen size
        const checkScreenSize = () => {
            if (window.innerWidth <= 768) {
                hamburger.style.display = 'block';
                nav.style.display = nav.classList.contains('mobile-active') ? 'block' : 'none';
            } else {
                hamburger.style.display = 'none';
                nav.style.display = 'block';
                nav.classList.remove('mobile-active');
            }
        };
        
        window.addEventListener('resize', checkScreenSize);
        checkScreenSize();
    };
    
    // Initialize mobile menu
    createMobileMenu();
    
    // Add loading animation for images
    const images = document.querySelectorAll('img');
    images.forEach(img => {
        img.addEventListener('load', function() {
            this.style.opacity = '1';
            this.style.transition = 'opacity 0.3s ease';
        });
        
        // Set initial state
        img.style.opacity = '0';
        
        // If image is already loaded
        if (img.complete) {
            img.style.opacity = '1';
        }
    });
    
    // Add hover effects for interactive elements
    const interactiveElements = document.querySelectorAll('.research-card, .publication-item, .person-card');
    interactiveElements.forEach(el => {
        el.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-5px)';
        });
        
        el.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });
    
    // Add typing effect for hero title (optional enhancement)
    const addTypingEffect = () => {
        const heroTitle = document.querySelector('.hero-text h1');
        if (heroTitle) {
            const text = heroTitle.textContent;
            heroTitle.textContent = '';
            heroTitle.style.borderRight = '2px solid #2c3e50';
            
            let i = 0;
            const typeWriter = () => {
                if (i < text.length) {
                    heroTitle.textContent += text.charAt(i);
                    i++;
                    setTimeout(typeWriter, 100);
                } else {
                    // Remove cursor after typing is complete
                    setTimeout(() => {
                        heroTitle.style.borderRight = 'none';
                    }, 1000);
                }
            };
            
            // Start typing effect after a short delay
            setTimeout(typeWriter, 1000);
        }
    };
    
    // Uncomment to enable typing effect
    // addTypingEffect();
    
    // Add parallax effect for hero section
    window.addEventListener('scroll', function() {
        const scrolled = window.pageYOffset;
        const heroSection = document.querySelector('.hero-section');
        
        if (heroSection && scrolled < window.innerHeight) {
            heroSection.style.transform = `translateY(${scrolled * 0.5}px)`;
        }
    });
    
    // Form validation (if contact form is added later)
    const handleFormSubmission = (form) => {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Add form validation logic here
            const formData = new FormData(form);
            
            // Simulate form submission
            console.log('Form submitted:', Object.fromEntries(formData));
            
            // Show success message
            const successMessage = document.createElement('div');
            successMessage.textContent = 'Message sent successfully!';
            successMessage.style.background = '#4CAF50';
            successMessage.style.color = 'white';
            successMessage.style.padding = '1rem';
            successMessage.style.borderRadius = '4px';
            successMessage.style.marginTop = '1rem';
            
            form.appendChild(successMessage);
            
            // Remove success message after 3 seconds
            setTimeout(() => {
                successMessage.remove();
            }, 3000);
            
            // Reset form
            form.reset();
        });
    };
    
    // Initialize form handling if contact form exists
    const contactForm = document.querySelector('#contact-form');
    if (contactForm) {
        handleFormSubmission(contactForm);
    }
    
    // Add search functionality (for future enhancement)
    const addSearchFunctionality = () => {
        // This can be expanded to add search across publications, news, etc.
        const searchInput = document.querySelector('#search-input');
        if (searchInput) {
            searchInput.addEventListener('input', function() {
                const query = this.value.toLowerCase();
                const searchableElements = document.querySelectorAll('[data-searchable]');
                
                searchableElements.forEach(el => {
                    const text = el.textContent.toLowerCase();
                    if (text.includes(query) || query === '') {
                        el.style.display = 'block';
                    } else {
                        el.style.display = 'none';
                    }
                });
            });
        }
    };
    
    // Initialize search functionality
    addSearchFunctionality();
});

// Utility functions
const utils = {
    // Smooth scroll to element
    scrollToElement: (element, offset = 0) => {
        const targetPosition = element.offsetTop - offset;
        window.scrollTo({
            top: targetPosition,
            behavior: 'smooth'
        });
    },
    
    // Debounce function for performance
    debounce: (func, wait) => {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    },
    
    // Check if element is in viewport
    isInViewport: (element) => {
        const rect = element.getBoundingClientRect();
        return (
            rect.top >= 0 &&
            rect.left >= 0 &&
            rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
            rect.right <= (window.innerWidth || document.documentElement.clientWidth)
        );
    }
};

// Export utilities for potential use in other scripts
window.LabWebsiteUtils = utils;