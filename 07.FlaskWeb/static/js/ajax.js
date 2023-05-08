// AJAX(Asynchronous Javascript and XML)
// Web page의 일부분을 변경하는 방법

function changeQuote() {
    $.ajax({
        type: 'GET',
        url: '/change_quote',
        data: ' ',                 // 서버로 전달할 데이터
        success: function(msg) {     // msg: 서버로부터 받은 데이터
            $('#quoteMsg').html('msg');
        }
    });
}
function changeAddr() {
        $('#addrInput').attr('class', 'mt-2')	// input box가 보이게
}
function addrSubmit() {
        $('#addrInput').attr('class', 'mt-2 d-none');	// input box가 안보이게
        let addr = $('#addrInputTag').val();	// input 값
        $.ajax({
            type: 'GET',
            url: '/change_addr',
            data: {addr: addr},		// addr로 읽어라 : addr(위에서 변수 선언한 addr)
            success: function(msg) {
                $('#addr').html(msg);
            }
        });
}
function changeWeather() {
    let addr = $('#addr').text();
    $.ajax({
        type: 'GET',
        url: '/weather',
        data: {addr: addr},
        success: function(result) {
            $('#weather').html(result);	// 아래 weather자리에 result값을 주어라
        }
    });
}