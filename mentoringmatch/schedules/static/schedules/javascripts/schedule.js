/* Start and end times on the schedule */
var START_TIME = 8;

/* Minutes in an hour */
var HOUR_LENGTH = 60;

/* Determines the number of pixels from the top of the table for offsetting
 * elements in the calendar
 * @param time - a string in "hh:mm" format, where the hour is defined in
 *  24-hour time.
 */
function get_vertical_offset( time ){

    var time_array = time.split( ":" );
    var hour = parseInt( time_array[0], 10 );
    var minute = parseInt( time_array[1], 10 );

    var rows = $(".calendar tbody").first().children();

    var offset = 0;
    var current_row = rows.first();
    for( var i = 0; i < rows.length && i + START_TIME < hour; i++ ){
        offset += current_row.height();
        current_row = current_row.next();
    }

    offset += minute * current_row.height() / HOUR_LENGTH;

    return offset;
}

$(document).ready(function(){

    // Position slots correctly on the schedule
    $(".day li").each(function( i, item ){
        var start = $(this).data( "start" );
        var end = $(this).data( "end" );

        var top_offset = get_vertical_offset( start );
        var bottom_offset = get_vertical_offset( end );

        $(this).css( "top", top_offset );
        $(this).height( bottom_offset - top_offset - 6 );
    });

});
