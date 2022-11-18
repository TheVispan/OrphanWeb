//Функция множественного удаления
$(function() { //Функция при вызове декйствиях в блоке филтров и поиска
    $(document).on("click", "#delete", function(){
        var items = [];
        $("#item:checked").each(function(i, item) {
            items.push($(item).attr("value"))
        });
        $.ajax({
        type: "POST",
        url: "/users/delete/", //Куда отправляется запрос
        data: {
           'items' : items,
           'csrfmiddlewaretoken': $('[name=csrfmiddlewaretoken]').val()
        },
        success: function(data){
            for (let i = 0; i < items.length; i++){
                $(".user-" + items[i]).remove();
            }
        },
        })
    });
});

