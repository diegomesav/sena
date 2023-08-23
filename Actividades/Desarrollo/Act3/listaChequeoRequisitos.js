const ol = document.querySelector("ol");
const criterios = ["  crit 1", " crit 2"];

for(const criterio of criterios){
    for(let i = 0; i < 4; i++){
        const checbox = document.createElement("input");
        checbox.type = "checkbox";
        ol.appendChild(checbox);
    }
    const label = document.createElement("label");
    const br = document.createElement("br");
    label.textContent = criterio;
    cuerpo.appendChild(label);
    cuerpo.appendChild(br);
}