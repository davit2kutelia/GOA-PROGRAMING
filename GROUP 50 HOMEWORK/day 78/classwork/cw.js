// let p = document.querySelector("p")
// p.style.color = "red"


let body = document.body
let div = document.createElement("div")

let divTwo = document.createElement('div')
div.appendChild(divTwo)

body.appendChild(div)

let divTree = document.createElement("div")
div.appendChild(divTree)

div.style.width = "200px"
div.style.height = "200px"


divTwo.style.width = "200px"
divTwo.style.height = "200px"
divTwo.style.backgroundColor = "blue"
divTwo.style.marginBottom = "20px"



divTree.style.width = "200px"
divTree.style.height = "200px"
divTree.style.backgroundColor = "red"

