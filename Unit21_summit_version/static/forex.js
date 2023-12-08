const allowCurrencies = ['AUD','CAD','CHF','CNY','EUR','GBP','HKD','INR','JPY','KRW','MXN','NZD','SGD','THB','USD'];
const $cfrom = $(".cfrom");
const $cto = $(".cto");
let $amount = $(".amount");

function showMessage(msg) {
    $(".msg").text(msg);
}
    
    
$('.forex-form').on('click',function(e){
    
    let cfrom = $cfrom.val();
    let cto = $cto.val();
    let amount = $amount.val();

    if (!allowCurrencies.includes(cfrom.toUpperCase()) && cfrom !== ""){
        msg = 'Not a valid code:${cfrom}'
        showMessage(`Not a valid code:${cfrom}`);
        e.preventDefault();
    }
    else if (!allowCurrencies.includes(cto.toUpperCase()) && cto !== ""){
        showMessage
        showMessage(`Not a valid code:${cto}`);
        e.preventDefault();
    }
    else if (amount <=0 && amount !== ""){
        showMessage('Not a valid amount.');
        e.preventDefault();
    }
    else {
        showMessage('');
    }
})
 