const criterios = [
"¿Se dispone de un servidor dedicado?",
"¿Cuál es el costo mensual y anual del servidor dedicado?",
"¿El servidor dedicado cuenta con la potencia y recursos necesarios?",

"¿Cuál es el costo mensual y anual del servicio de alojamiento?",
"¿Cuántos GB de almacenamiento se incluyen en el plan mensual?",
"¿El almacenamiento ofrecido es suficiente para las necesidades del software?",

"¿Cuánta memoria RAM se recomienda para un rendimiento óptimo?",
"¿Cuál es el costo adicional mensual de la memoria RAM?",
"¿La cantidad de memoria RAM propuesta es adecuada para el software?",

"¿Existe un procesador potente disponible?",
"¿Cuál es el costo adicional mensual del procesador más potente?",
"¿El procesador seleccionado cumple con los requisitos del software?",


"¿Qué sistema operativo se utilizará en el servidor?",
"¿El proveedor de hosting ofrece sistemas operativos gratuitos?",
"¿Cuál es el costo anual del sistema operativo seleccionado?",

"¿Se necesita un servidor web específico, como Apache o Nginx?",
"¿El proveedor de hosting ofrece servidores web específicos de forma gratuita?",
"¿El servidor web es el adecuado para el proyecto?",

"¿Se utilizará una base de datos como MySQL o PostgreSQL?",
"¿Existen costos adicionales asociados al uso de estas bases de datos?",
"¿la bases de datos cumple con los estandares necesarios de calidad y seguridad para la informacion?",

"¿Se requiere un certificado SSL para garantizar la seguridad del sitio web?",
"¿Cuál es el costo anual promedio de un certificado SSL estándar o de validación de dominio?",

"¿Se contratarán servicios de mantenimiento y soporte técnico?",
"¿Cuáles son los costos asociados a estos servicios?",
"¿El nivel de servicio requerido cumple con las necesidades del software?",


"¿El procesador del cliente cumple con los requisitos mínimos de al menos un procesador de doble núcleo a 2 GHz o superior?",
"¿El cliente posee un procesador adecuado recomendado?",
"¿El cliente posee un procesador compatible con el sistema?",

"¿La memoria RAM del cliente cumple con los requisitos mínimos de al menos 4 GB o más?",
"¿El cliente posee memoria RAM de 8 GB recomendada?",
"¿El cliente posee una RAM en buen estado fisico?",

"¿La tarjeta gráfica del cliente cumple con los requisitos mínimos de una tarjeta gráfica dedicada con al menos 1 GB de memoria?",
"¿El cliente posee una tarjeta gráfica adecuada recomendada?",
"¿El cliente posee una tarjeta gráfica en buen estado fisico?",

"¿El cliente dispone de la capacidad de almacenamiento requerida?",
"¿El cliente posee un disco duro aproximado del almacenamiento recomendado?",
"¿El cliente posee un disco duro o almacenamiento en buen estado fisico?",


"¿El cliente utiliza un sistema operativo compatible, como Windows, macOS o Linux?",

"¿El cliente utiliza un navegador web moderno y actualizado, como Google Chrome, Mozilla Firefox o Microsoft Edge?",

"¿El cliente tiene instalados los complementos necesarios, como Adobe Flash Player u otros reproductores multimedia adicionales?",

"¿El cliente dispone de una conexión a Internet estable y de alta velocidad?",
"¿El cliente posee conexión a Internet mensualmente?",

"¿El cliente realiza regularmente las actualizaciones de software recomendadas?",
"¿Existen costos asociados a las actualizaciones y el mantenimiento del software utilizado?",
];

const ol = document.querySelector("ol");
for(const criterio of criterios){
    const li = document.createElement("li");
    for(let i = 0; i < 4; i++){
        const checbox = document.createElement("input");
        checbox.type = "checkbox";
        li.appendChild(checbox);
    }
    const label = document.createElement("label");
    const div = document.createElement("div");
    label.textContent = criterio;
    li.appendChild(label);
    li.appendChild(div)
    ol.appendChild(li);
}