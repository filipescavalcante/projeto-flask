const addItemBtn = document.querySelector('#add-item')
const submitBtn = document.querySelector('#submit')
const closeBtn = document.querySelector('#close-form')

const main = document.querySelector('main')
const form = document.querySelector('form')
const addItemText = document.querySelector('p')
const inputs = [...document.querySelectorAll('input[type="text"]')]
const table = document.querySelector('table')
const tableContent = document.querySelector('tbody')

addItemBtn.addEventListener('click', () => {
    form.style.display = 'flex'
    addItemText.style.display = 'none'
})

closeBtn.addEventListener('click', () => {
    form.style.display = 'none'
    addItemText.style.display = 'block'

    form.reset()
    }
)

submitBtn.addEventListener('click', () => {
    form.submit()
})

const verifyContent = () => {
    if (tableContent.children.length == 0) {
        table.style.display = 'none'
    } else {
        table.style.display = 'block'
    }
}

verifyContent()

