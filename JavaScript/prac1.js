const title = document.querySelector("#title");

const base_color = "red";
const other_color = "blue";

function handleClick(){
    const currentColor = title.style.color;
    if (currentColor === base_color){
        title.style.color = other_color;
    } else{
        title.style.color = base_color;
    }
}

function init(){
    title.style.color = base_color;
    title.addEventListener("click", handleClick);
}

init();
