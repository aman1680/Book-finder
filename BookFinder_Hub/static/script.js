function toggleForms() {
    var searching = false;
    var taskSelect = document.getElementById("task-select");
    var uploadForm = document.getElementById("upload-form");
    var searchForm = document.getElementById("search-form");

    if(taskSelect.value == "select") {
        uploadForm.style.display = "none";
        searchForm.style.display = "none";
    } else if (taskSelect.value == "upload") {
        uploadForm.style.display = "block";
        searchForm.style.display = "none";
    } else if (taskSelect.value == "search") {
        uploadForm.style.display = "none";
        searchForm.style.display = "block";
    }
}