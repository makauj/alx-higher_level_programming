$(document).ready(function() {
    $.getJSON(
        "https://api.github.com/users/yourusername/repos", function(data) {
                data.results.forEach(function(film) {
            $('<li>').text(film.title).appendTo('ul#repos');
        });
    });
});
