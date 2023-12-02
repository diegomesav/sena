const urls = [
    "https://www.youtube.com/embed/U709qY6S9rA?si=Jvm5P19wZgDraPKf",
    "https://www.youtube.com/embed/coK4jM5wvko?si=KCgBJxnLyY2c1ZpH",
    "https://www.youtube.com/embed/F0ILFYl8YgI?si=BII-jnApli_NfiNO",
]

const courses = [
    "Java"
]



const divContainer = document.querySelector("div");
divContainer.className = "container"

const section = document.createElement("section");
section.className = "card-section"

let indexCourse = 0
for (const url of urls){

    const divP = document.createElement("div");
    divP.className = "tarjeta"

    const divTitle = document.createElement("div");
    divTitle.className = "titulo"
    divTitle.textContent = "Curso de " + courses[indexCourse]
    indexCourse

    const divBody = document.createElement("div");
    divBody. className = "cuerpo"

    const iframe = document.createElement("iframe");
    iframe.width = "460"
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
    section.appendChild(divP)
}

divContainer.appendChild(section);

