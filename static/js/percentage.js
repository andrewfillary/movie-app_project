// Changes stroke colour based on the percentage value

$(function() {
    // loops through all <path> elements with the class 'circle'
    $('path.circle').each(function() {
        // $(this) refers to the current <path> element
        // gets the text value of the first <text> child element
        var score = parseInt($(this).siblings('text').first().text());
        var color = 'green';
        if (score <= 30) {
            color = 'red';
        }
        else if (score <= 70) {
            color = 'orange';
        }
        // set the color of the current element
        $(this).css('stroke', color);
    })
});