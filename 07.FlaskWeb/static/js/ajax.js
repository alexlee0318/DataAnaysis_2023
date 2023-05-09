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

let flig = false;
function changeAddr() {
    if (!flig) {
        $('#addrInput').attr('class', 'mt-2'); 
        flig = !flig;
    } else {
        $('#addrInput').attr('class', 'mt-2 d-none');
        flig = !flig;
    }
}
function addrSubmit() {
        // $('#addrInputTag').attr('type', 'text d-none');
        $('#addrInput').attr('class', 'mt-2 d-none');	// input box가 안보이게
        let addr = $('#addrInputTag').val();	// input 값
        $.ajax({
            type: 'GET',
            url: '/change_addr',
            data: {addr: addr},		// addr로 읽어라 : addr(위에서 변수 선언한 addr)
            success: function(msg) {
                $('#addr').html(msg);
                addr = !addr;
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

let flag = false;   // flag: 임의의 변수. 함수 바깥에 전역변수로 설정
function changeProfile() {
    if (!flag) {
        $('#imageInput').attr('class', 'mt-2'); 
        flag = !flag;
    } else {
        $('#imageInput').attr('class', 'mt-2 d-none');
        flag = !flag;
    }
}
  function imageSubmit() {
    let imageInputVal = $('#image')[0];
    let formData = new FormData();
    formData.append('image', imageInputVal.files[0]);
    $.ajax({
        type: 'POST',
        url: '/change_profile',
        data: formData,
        processData: false,
        contentType: false,
        success: function(result) {
            $('#imageInput').attr('class', 'mt-2 d-none');
            let fname = 'http://127.0.0.1:5000/static/data/profile.png?q=' + result;
            $('#profile').attr('src', fname);
        }
    });
  }