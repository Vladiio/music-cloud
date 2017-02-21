$(document).ready( function(){

    $('#add-comment-btn').click( function(event){

        var text = $('#id_text').val()
        var songid = $(this).attr('data-songid');
        var author = $(this).attr('data-author');
        var csrf_token = $('meta[name="csrf-token"]').attr('content');

        var context = {
            song_id: songid,
            author_name: author,
            text_body: text
        }
        $.get('/add_comment/', context, function(data){

            $('#comment-list').html(data);
        });
    });
});