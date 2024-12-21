document.addEventListener("DOMContentLoaded", function () {
    const rows = document.querySelectorAll(".language-row");

    rows.forEach(row => {
        row.addEventListener("click", function () {
            const lang = this.dataset.lang;
            const bookRow = document.getElementById(`books-${lang}`);
            
            if (bookRow.style.display === "none") {
                bookRow.style.display = "table-row";
            } else {
                bookRow.style.display = "none";
            }
        });
    });
});
