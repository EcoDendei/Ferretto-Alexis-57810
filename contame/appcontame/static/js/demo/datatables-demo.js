// Call the dataTables jQuery plugin
//$(document).ready(function() {
//  $('#dataTable').DataTable();
//});


$(document).ready(function() {
  $('#dataTable').DataTable({language: {
    "decimal":        "",
    "emptyTable":     "No hay datos disponibles en la tabla",
    "info":           "Mostrando _START_ a _END_ de _TOTAL_ entries",
    "infoEmpty":      "Mostrando 0 a 0 de 0 entradas",
    "infoFiltered":   "(filtrado de _MAX_ entradas totales)",
    "infoPostFix":    "",
    "thousands":      ",",
    "lengthMenu":     "Mostrando _MENU_ entradas",
    "loadingRecords": "Cargando...",
    "processing":     "",
    "search":         "Buscar:",
    "zeroRecords":    "No se encontraron coincidencias",
    "paginate": {
        "first":      "Primero",
        "last":       "Último",
        "next":       "Siguiente",
        "previous":   "Anterior"
    },
    "aria": {
        "orderable":  "Ordenar por esta columna",
        "orderableReverse": "Ordenar al reves por esta columna"
    }
}});
});