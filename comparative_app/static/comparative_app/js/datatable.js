// Datatables script
function getDT(){
    var table = $("#value_by_affixal_morphemes").DataTable({
        // Datatables configurations
        processing: true,
        serverSide: true,
        ajax: {
            url: '/api/language/?format=datatables',
            dataType: 'json',
            type: 'GET',
            // dataSrc: function(response) {
            //     var cols = [];
            //     var data = response.data[0];
            //     for (var key in data) {
            //         if (data.hasOwnProperty(key)) {
            //             cols.push({data: key, title: key});
            //         }
            //     }
            //     return {
            //         data: response.data,
            //         columns: cols
            //     };
            // }
        },
        // columns: function(response) {
        //     console.log(response.data)
        //     var cols = [];
        //     var data = response.data[0];
        //     for (var key in data) {
        //         if (data.hasOwnProperty(key)) {
        //             cols.push({data: key});
        //         }
        //     }
        //     return cols;
        // },
        paging: true,
        pageLength: 10,
        lengthChange: true,
        autoWidth: false,
        searching: true,
        // bInfo: true,
        // bSort: true,
        scrollX: true,
        fixedColumns: {left: 1},
        stateSave: false, //saving state when updating page
    
        columns: [
            {'data': 'gram_value'},
            {'data': 'Азербайджанский'},
            {'data': 'Алтайский'},
            {'data': 'Башкирский'},
            {'data': 'Гагаузский'},
            {'data': 'Долганский'},
            {'data': 'Казахский'},
            {'data': 'Караимский (Галичский диалект)'},
            {'data': 'Караимский (Тракайский диалект)'},
            {'data': 'Каракалпакский'},
            {'data': 'Карачаево-балкарский'},
            {'data': 'Кашкайский'},
            {'data': 'Киргизский'},
            {'data': 'Крымскотатарский'},
            {'data': 'Крымчакский'},
            {'data': 'Кумандинский'},
            {'data': 'Кумыкский'},
            {'data': 'Ногайский'},
            {'data': 'Ортатюрк'},
            {'data': 'Саларский'},
            {'data': 'Сибирско-татарский'},
            {'data': 'Татарский'},
            {'data': 'Телеутский'},
            {'data': 'Тофаларский'},
            {'data': 'Тувинский'},
            {'data': 'Турецкий'},
            {'data': 'Туркменский'},
            {'data': 'Узбекский (Кириллица)'},
            {'data': 'Узбекский (Латиница)'},
            {'data': 'Уйгурский'},
            {'data': 'Урумский'},
            {'data': 'Хакасский'},
            {'data': 'Халаджский'},
            {'data': 'Чалканский'},
            {'data': 'Чувашский'},
            {'data': 'Чулымский'},
            {'data': 'Шорский'},
            {'data': 'Якутский (Саха)'}
        ],
        "language": 
        {
            "info": "Показано с _START_ по _END_ из _TOTAL_ записей",
            "infoFiltered":   "(отобрано из _MAX_ записей)",
            "search": "Поиск:",
            "paginate": {
                "next": "Дальше",
                "previous": "Назад"
            },
        },
        
        "columnDefs": [
            {
                "width": 30,
                "targets": [0],
                "visible": true,
            },
            {
                "targets": '_all',
                "visible": false
                // "searchable": false
            },
        ],
    
        dom: 'lBfrtip',
        buttons: [
        {
            extend: 'collection',
            text: 'Сохранить как',
            background: false,
            className: 'blue',
            buttons: [
                {
                    extend: 'copyHtml5',
                    text: 'Копировать',
                    exportOptions: {
                        columns: [ 0, ':visible' ]
                    }
                },
                {
                    extend: 'excelHtml5',
                    exportOptions: {
                    columns: ':visible'
                    }
                },
                {
                    extend: 'pdfHtml5',
                    exportOptions: {
                        columns: ':visible'
                    }
                },
            ]
        },
        {
            extend: 'colvis',
            text: 'Язык выбора',
            columns: 'th:nth-child(n+2)',
            collectionLayout: 'dropdown columns',
            popoverTitle: 'Выберите язык:',
            background: false,
            className: 'blue',
        }
        ]
    });

}
$(document).ready(function(){
    getDT();
})