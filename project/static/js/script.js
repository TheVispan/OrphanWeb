//Функция удаления контексного меню
function removeMenu (elem){
    for (let j = 0; j < elem.length; j++){
        elem[j].style.display = "none"

    }
}

//функция контексного меню
document.onclick = function (e) {
    var obj = document.querySelectorAll(".table-blocks")
    var elem = document.querySelectorAll(".context-menu")
//Условие для ограничения срабатывания контексного меню
    if (e.target.className != "context-menu" && e.target.className != "table-block") {
        removeMenu (elem)//вызов функции удаления
    }
    if (e.target.className == "table-block") {

        for (let i = 0; i < obj.length; i++){
            obj[i].addEventListener('click', e => {
                removeMenu (elem)//вызов функции удаления
                //переворачиваем меню при столкновение с краями экрана
                if (e.pageY > document.documentElement.clientHeight + document.documentElement.scrollTop - 100){
                    elem[i].style.transform = "translate(0, -100%)"
                } else if (e.pageX > body.getBoundingClientRect().right - 166){
                    elem[i].style.transform = "translate(-100%, -100%)"
                } else {
                    elem[i].style.transform = ""
                }
                //Делаем блок видимым и устанавливаем координаты x и y
                elem[i].style.top = e.pageY + "px"
                elem[i].style.left = e.pageX + "px"
                elem[i].style.display = "flex"

            })
            obj[i].removeEventListener('click', e)//удаляем обработчик событий

        }
    }
}

/*Функция удаления контексного меню при прокручивания колесика мыши
window.onscroll = function(e){
    var elem = document.querySelectorAll(".context-menu")
    removeMenu (elem)

}
*/











