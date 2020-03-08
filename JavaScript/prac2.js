const title = document.querySelector("#title");

const CLCIKED_CLASS = "clicked";
const BASIC_CLASS = "btn";

// 3번째방법(toggle사용)
function handleColor(){
    title.classList.toggle(CLCIKED_CLASS);
}

/* 2번째방법(conatains사용)
function handleColor(){
    const hasClass = title.classList.contains(CLCIKED_CLASS);
    if (hasClass){
        title.classList.remove(CLCIKED_CLASS);
    } else{
        title.classList.add(CLCIKED_CLASS);
    }
}
*/
/* 1번째방법(가장풀어쓰기)
function handleColor(){
    const currentClass = title.className;
    if (currentClass === BASIC_CLASS){
        title.classList.add(CLCIKED_CLASS);
    } else{
        title.classList.remove(CLCIKED_CLASS);
    }
}
*/

function init(){
    title.className = BASIC_CLASS;
    title.addEventListener("click", handleColor);
}

init();

