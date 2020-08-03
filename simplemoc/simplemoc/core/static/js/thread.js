$(".reply-cancel-correct-lnk").on("click", function (e) {
    e.preventDefault();
    var $this = $(this);
    var $p = $this.closest("p");
    $.get($this.attr('href'), function (data) {
        if (data.success) {
            $p.find(".reply-correct-msg").addClass('hidden');
            $this.addClass('hidden');
            $p.find('.reply-correct-lnk').removeClass('hidden');
        } else {
            alert(data.message);
        }
    }, "json");
    return false;
});

$('.reply-correct-lnk').on('click', function (e) {
    e.preventDefault();
    var $this = $(this);
    var $p = $this.closest("p");
    $.get($this.attr('href'), function (data) {
        if (data.success) {
            $("#div-comments .reply-correct-msg").addClass('hidden');
            $("#div-comments .reply-cancel-correct-lnk").addClass('hidden');
            $("#div-comments .reply-correct-lnk").removeClass('hidden');

            $p.find(".reply-correct-msg").removeClass('hidden');
            $this.addClass('hidden');
            $p.find('.reply-cancel-correct-lnk').removeClass('hidden');
        } else {
            alert(data.message)
        }
    }, 'json');
    return false;
})
