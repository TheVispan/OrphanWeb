//Функция для чекбокса отчисленных
function isChecked() {
    if (document.getElementById("expelled").checked) {
        document.getElementById('date-of-deduction').style.display = "flex"
    } else {
        document.getElementById('date-of-deduction').style.display = "none"
    }
}

//Функции поиска
function search(){
    $.ajax({
        type: "GET",
        url: "/search", //Куда отправляется запрос
        data: { //Что отправляется
            'from_birthdate' : $('#fromBirthdate').val(),
            'to_birthdate' : $('#toBirthdate').val(),
            'from_date_of_receipt' : $('#fromDateOfReceipt').val(),
            'to_date_of_receipt' : $('#toDateOfReceipt').val(),
            'from_date_of_deduction' : $('#fromDateOfDeduction').val(),
            'to_date_of_deduction' : $('#toDateOfDeduction').val(),
            'orphan' : $('#orphan').is(':checked'),
            'disable' : $('#disable').is(':checked'),
            'expelled' : $('#expelled').is(':checked'),
            'select_group' : $("#groupComboBox option:selected").val(),
            'select_gender' : $("#genderComboBox option:selected").val(),
            'search_text' : $('#search').val(),

        },
        dataType: 'json', //Тип данных которые придут
        success: function (data) { //Функция при успешном запросе
            list = JSON.parse(data)
            let orphansList = ""
            for (item in list) {
                orphansList += getOrphanListItemHTML(list[item])
            }
            document.getElementById('body').innerHTML = orphansList
        }
    });
} search();

$(function() { //Функция при вызове декйствиях в блоке филтров и поиска
    $('#searchAndFilteringPanel').change(search).keyup(search);
});

//Функция множественного удаления
$(function() { //Функция при вызове декйствиях в блоке филтров и поиска
    $(document).on("click", "#delete", function(){
        var items = [];
        $("#item:checked").each(function(i, item) {
            items.push($(item).attr("value"))
        });
        console.log(items)
        $.ajax({
        type: "POST",
        url: "delete/", //Куда отправляется запрос
        data: {
           'items' : items,
           'csrfmiddlewaretoken': $('[name=csrfmiddlewaretoken]').val()
        },
        success: search(),
        })
    });
});

function getOrphanListItemHTML(orphan) {

    if (orphan.fields.orphan == 1){
        orphanCheckbox = "Да"
    } else {
        orphanCheckbox = "Нет"
    }
    if (orphan.fields.gender == 1){
        orphanGender = "Муж"
    } else {
        orphanGender = "Жен"
    }
    return`
            <tr class="table-blocks">
            <th class="table-block-checkbox"><input type="checkbox" id="item" value="${ orphan.pk }"></th>
            <td class="table-block">${ orphan.fields.name }</td>
            <td class="table-block">${ orphanGender }</td>
            <td class="table-block">${ orphan.fields.dateofbirth.substr(0,10) }</td>
            <td class="table-block">${ orphan.fields.placeofbirth }</td>
            <td class="table-block">${ orphanCheckbox }</td>
            <td class="table-block">${ orphan.fields.dateofreceipt.substr(0,10) }</td>
            <td class="table-block">${ orphan.fields.dateofdeduction.substr(0,10) }</td>
            </tr>
            <div class = "btn-group-vertical context-menu">
                <div class="dropdown-menu-verical">
                    <a class="dropdown-item" href="${orphan.pk}/change/">Карта воспитанника</a>
                </div>
            </div>`
    }