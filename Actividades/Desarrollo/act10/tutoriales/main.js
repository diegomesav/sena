const urls = [
    "https://www.youtube.com/embed/G2FCfQj-9ig?si=aWTfnoecHs2qg3eU",
    "https://www.youtube.com/embed/U709qY6S9rA?si=Jvm5P19wZgDraPKf"
]

const courses = [
    "Python", "Java"
]

const body = document.querySelector("body");
let indexCourse = 0
for (const url of urls){

    const divP = document.createElement("div");
    divP.className = "tarjeta"

    const divTitle = document.createElement("div");
    divTitle.className = "titulo"
    divTitle.textContent = "Curso de " + courses[indexCourse]
    indexCourse++

    const divBody = document.createElement("div");
    divBody. className = "cuerpo"

    const iframe = document.createElement("iframe");
    iframe.width = "480"
    iframe.height = "315"
    iframe.src = url
    iframe.title = "YouTube video player"
    //iframe.frameBorder = "0"
    iframe.allow = "accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    iframe.allowFullscreen

    const divFootter = document.createElement("div");
    divFootter.className = "pie"
    divFootter.textContent = "ste es un curso bastante completo y está diseñado para personas sin conocimientos en programación"

    divP.appendChild(divTitle);
    divBody.appendChild(iframe);
    divP.appendChild(divBody);
    divP.appendChild(divFootter);
    body.appendChild(divP)
}
