/* Show Menu */
const navMenu = document.getElementById('nav-menu'),
      navToggle = document.getElementById('nav-toggle'),
      navClose = document.getElementById('nav-close')

/* Menu Show */
/* Validate if constant exists */
if(navToggle){
    navToggle.addEventListener('click', () =>{
        navMenu.classList.add('show-menu')
    })
}

/* Menu Hidden */
/* Validate if constant exists */
if(navClose){
    navClose.addEventListener('click', () =>{
        navMenu.classList.remove('show-menu')
    })
}
/* Search Section Show */
document.querySelector('.home__button').addEventListener('click', function() {
    document.getElementById('search').style.display = 'block';
});
document.querySelector('.feature__button').addEventListener('click', function() {
    document.getElementById('search').style.display = 'block';
});

/* Remove Menu Mobile */
const navLink = document.querySelectorAll('.nav__link')

const linkAction = () =>{
    const navMenu = document.getElementById('nav-menu')
    // When we click on each nav__link, we remove the show-menu class
    navMenu.classList.remove('show-menu')
}
navLink.forEach(n => n.addEventListener('click', linkAction))


/* Blur Header */
const blurHeader = () =>{
    const header = document.getElementById('header')
    // When the scroll is greater than 50 viewport height, add the blur-header class to the header tag
    this.scrollY >= 50  ? header.classList.add('blur-header')
                        : header.classList.remove('blur-header')
}
window.addEventListener('scroll', blurHeader)

/* Show Scroll Up */
const scrollUp = () =>{
    const scrollUp = document.getElementById('scroll-up')
    this.scrollY >= 350 ? scrollUp.classList.add('show-scroll')
                        : scrollUp.classList.remove('show-scroll')
}
window.addEventListener('scroll', scrollUp)

/* Scroll Section Active Link */
const sections = document.querySelectorAll('section[id')

const scrollAcive = () =>{
    const scrollDown = window.scrollY

    sections.forEach(current =>{
        const sectionHeight = current.offsetHeight,
              sectionTop    = current.offsetTop - 58,
              sectionId     = current.getAttribute('id'),
              sectionClass  = document.querySelector('.nav__menu a[href*=' + sectionId + ']')
              
        if(scrollDown > sectionTop && scrollDown <= sectionTop + sectionHeight){
            sectionClass.classList.add('active-link')
        }else {
            sectionClass.classList.remove('active-link')
        }
    })
}
window.addEventListener('scroll', scrollAcive)

/* Scroll Reveal Animation */

const sr = ScrollReveal({
    origin: 'top',
    distance: '60px',
    duration: 2500,
    delay: 400,
    //reset: true, //animations repeat
})

sr.reveal(`.home__social, .sponsor__container. footer`)
sr.reveal(`.home__title span:nth-child(1)`, {origin: 'left', opacity: 1})
sr.reveal(`.home__title span:nth-child(2)`, {origin: 'left', opacity: 1})
sr.reveal(`.home__title span:nth-child(3)`, {origin: 'left', opacity: 1})
sr.reveal(`.home__title span:nth-child(4)`, {origin: 'right', opacity: 1})
sr.reveal(`.home__title span:nth-child(5)`, {origin: 'right', opacity: 1})
sr.reveal(`.home__title span:nth-child(6)`, {origin: 'right', opacity: 1})
sr.reveal(`.home__title span:nth-child(7)`, {origin: 'right', opacity: 1})
sr.reveal(`.home__tooltip, .home__button`, {origin: 'bottom'})
sr.reveal(`.about__data`, {origin: 'left'})
sr.reveal(`.about__img, .feature__tooltip`, {origin: 'right'})



const search = document.querySelector('.search__input'),
    table_rows = document.querySelectorAll('tbody tr'),
    table_headings = document.querySelectorAll('thead th');

// 1. Searching for specific data of HTML table
search.addEventListener('input', searchTable);

function searchTable() {
    table_rows.forEach((row, i) => {
        let table_data = row.textContent.toLowerCase(),
            search_data = search.value.toLowerCase();

        row.classList.toggle('hide', table_data.indexOf(search_data) < 0);
        row.style.setProperty('--delay', i / 25 + 's');
    })

    document.querySelectorAll('tbody tr:not(.hide)').forEach((visible_row, i) => {
        visible_row.style.backgroundColor = (i % 2 == 0) ? 'transparent' : '#0000000b';
    });
}

// 2. Sorting | Ordering data of HTML table

table_headings.forEach((head, i) => {
    let sort_asc = true;
    head.onclick = () => {
        table_headings.forEach(head => head.classList.remove('active'));
        head.classList.add('active');

        document.querySelectorAll('td').forEach(td => td.classList.remove('active'));
        table_rows.forEach(row => {
            row.querySelectorAll('td')[i].classList.add('active');
        })

        head.classList.toggle('asc', sort_asc);
        sort_asc = head.classList.contains('asc') ? false : true;

        sortTable(i, sort_asc);
    }
})


function sortTable(column, sort_asc) {
    [...table_rows].sort((a, b) => {
        let first_row = a.querySelectorAll('td')[column].textContent.toLowerCase(),
            second_row = b.querySelectorAll('td')[column].textContent.toLowerCase();

        if (!isNaN(first_row) && !isNaN(second_row)) {
            first_row = Number(first_row);
            second_row = Number(second_row);
        }

        return sort_asc ? (first_row < second_row ? -1 : 1) : (first_row > second_row ? -1 : 1);
    })
    .forEach(sorted_row => document.querySelector('tbody').appendChild(sorted_row));
}

