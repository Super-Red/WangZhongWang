#-*-coding:utf-8-*-

from bs4 import BeautifulSoup
html10 = '''
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">








<html>
<head>
<title>试算平衡表</title>


<link href="css/blue_text.css" rel="stylesheet" type="text/css">
<link href="css/netinnet_css.css" rel="stylesheet" type="text/css">
<link href="css/softkf_common.css" rel="stylesheet" type="text/css">




<script>
    var _loginRole = 'M';   //login role
    var _sysRoleContral = '1';    //role contral
    var _sysTalkIM = '0'; //IM contral
    var _sysDecision = '1'; //??×÷????????
    var _bankruptcy = '0'
</script>
<script language="JavaScript" src="javascript/basic.js"></script>
<script language="JavaScript" src="javascript/operation.js"></script>
<script language="JavaScript" src="javascript/encoder.js"></script>
<script language="JavaScript" src="javascript/checkForm.js"></script>
<script language="JavaScript" src="javascript/jquery-1.6.1.min.js"></script>
<script language="JavaScript" src="javascript/dateSelect.js"></script>
<script type="text/javascript" src="javascript/multiTags.js"></script>
<script type="text/javascript" src="javascript/workStatus.js"></script>
<script language="JavaScript" src="javascript/softkf_common.js"></script>
<script language="JavaScript" src="javascript/MyQuickSelect.js"></script>
<script language="JavaScript" src="javascript/UrlManager.js"></script>
<script language="JavaScript" src="javascript/sandtable.js"></script>
<script language="JavaScript" src="javascript/loadmask/jquery.loadmask.js"></script>
<!-- 20150525 panyp add -->
<script language="JavaScript" src="javascript/browser.js?p=p"></script>
<link href="javascript/loadmask/jquery.loadmask.css" rel="stylesheet" type="text/css" />

<script language="JavaScript">
document.ondblclick=function(e){
    return false;
}
</script>

</head>
<body>
<div class="common_contentDiv">
    <form name="common_query" action="do" method="post" >
    <input type="hidden" name="action" value="dsh/dsh_statement" />
    <input id="start" type="hidden" name="start" value="trial_balance_statement" />
    <table class="tableNoLine" >
        <tr>
            <td align="left"><span class="titlePage">【试算平衡表】</span></td>
            <td align="right" nowrap="nowrap">年份:</td>
            <td>
                <select id="yyyy" name="yyyy" class="selectList">
                  <option value="" selected></option>
                  
                        <option value="2016">2016</option>
                    
                        <option value="2017">2017</option>
                    
                  
                </select>
            </td>
            <td align="right" nowrap="nowrap">月份:</td>
            <td>
                <select id="mm" name="mm" class="selectList">
                    <option value="" selected></option> 
                  
                    <option value="1">1</option>
                  
                    <option value="2">2</option>
                  
                    <option value="3">3</option>
                  
                    <option value="4">4</option>
                  
                    <option value="5">5</option>
                  
                    <option value="6">6</option>
                  
                    <option value="7">7</option>
                  
                    <option value="8">8</option>
                  
                    <option value="9">9</option>
                  
                    <option value="10">10</option>
                  
                    <option value="11">11</option>
                  
                    <option value="12">12</option>
                   
                </select>
            </td>
            <td align="right">
                <input id="btn_query" type="button" class="btnSubmit" value="查询" onclick="common_query.submit();" />
            </td>
        </tr>
    </table>
    </form>
    <table style="width:100%" class="tableGrid" border="1">
        <tr class="tableGridHeader" align="center">
            <td width="25%" colspan="2">科目</td>
            <td width="20%" colspan="2">期初余额</td>
            <td width="20%" colspan="2">本期发生额</td>
            <td width="20%" colspan="2">期末余额</td>
        </tr>
        <tr class="tableGridHeader" align="center">
            <td width="10%">代码</td>
            <td width="15%">名称</td>
            <td width="10%">借方</td>
            <td width="10%">贷方</td>
            <td width="10%">借方</td>
            <td width="10%">贷方</td>
            <td width="10%">借方</td>
            <td width="10%">贷方</td>
        </tr>
        
                <tr id="tr_1" class="rowGrid1" >
                    <div id="descr_1" style="display:none"></div>
                    <td align="left">
                        <div id="accountID_1">1001</div>
                    </td>
                    <td>
                        <div id="account_1">库存现金</div>
                    </td>
                    <td align="right">
                        <div id="opening_debit_1">0.00</div>
                    </td>
                    <td align="right">
                        <div id="opening_lend_1">0.00</div>
                    </td>
                    <td align="right">
                        <div id="current_debit_1">100000.00</div>
                    </td>
                    <td align="right">
                        <div id="current_lend_1">63719.91</div>
                    </td>
                    <td align="right">
                        <div id="endtime_debit_1">36280.09</div>
                    </td>
                    <td align="right">
                        <div id="endtime_lend_1">0.00</div>
                    </td>
                </tr>
            
                <tr id="tr_2" class="rowGrid0" >
                    <div id="descr_2" style="display:none"></div>
                    <td align="left">
                        <div id="accountID_2">1002</div>
                    </td>
                    <td>
                        <div id="account_2">银行存款</div>
                    </td>
                    <td align="right">
                        <div id="opening_debit_2">0.00</div>
                    </td>
                    <td align="right">
                        <div id="opening_lend_2">0.00</div>
                    </td>
                    <td align="right">
                        <div id="current_debit_2">23500167.85</div>
                    </td>
                    <td align="right">
                        <div id="current_lend_2">20920125.00</div>
                    </td>
                    <td align="right">
                        <div id="endtime_debit_2">2580042.85</div>
                    </td>
                    <td align="right">
                        <div id="endtime_lend_2">0.00</div>
                    </td>
                </tr>
            
                <tr id="tr_3" class="rowGrid1" >
                    <div id="descr_3" style="display:none"></div>
                    <td align="left">
                        <div id="accountID_3">1101</div>
                    </td>
                    <td>
                        <div id="account_3">交易性金融资产</div>
                    </td>
                    <td align="right">
                        <div id="opening_debit_3">0.00</div>
                    </td>
                    <td align="right">
                        <div id="opening_lend_3">0.00</div>
                    </td>
                    <td align="right">
                        <div id="current_debit_3">680.00</div>
                    </td>
                    <td align="right">
                        <div id="current_lend_3">38.00</div>
                    </td>
                    <td align="right">
                        <div id="endtime_debit_3">642.00</div>
                    </td>
                    <td align="right">
                        <div id="endtime_lend_3">0.00</div>
                    </td>
                </tr>
            
                <tr id="tr_4" class="rowGrid0" >
                    <div id="descr_4" style="display:none"></div>
                    <td align="left">
                        <div id="accountID_4">1122</div>
                    </td>
                    <td>
                        <div id="account_4">应收账款</div>
                    </td>
                    <td align="right">
                        <div id="opening_debit_4">0.00</div>
                    </td>
                    <td align="right">
                        <div id="opening_lend_4">0.00</div>
                    </td>
                    <td align="right">
                        <div id="current_debit_4">7319571.48</div>
                    </td>
                    <td align="right">
                        <div id="current_lend_4">0.00</div>
                    </td>
                    <td align="right">
                        <div id="endtime_debit_4">7319571.48</div>
                    </td>
                    <td align="right">
                        <div id="endtime_lend_4">0.00</div>
                    </td>
                </tr>
            
                <tr id="tr_5" class="rowGrid1" >
                    <div id="descr_5" style="display:none"></div>
                    <td align="left">
                        <div id="accountID_5">1221</div>
                    </td>
                    <td>
                        <div id="account_5">其他应收款</div>
                    </td>
                    <td align="right">
                        <div id="opening_debit_5">0.00</div>
                    </td>
                    <td align="right">
                        <div id="opening_lend_5">0.00</div>
                    </td>
                    <td align="right">
                        <div id="current_debit_5">2078049.19</div>
                    </td>
                    <td align="right">
                        <div id="current_lend_5">0.00</div>
                    </td>
                    <td align="right">
                        <div id="endtime_debit_5">2078049.19</div>
                    </td>
                    <td align="right">
                        <div id="endtime_lend_5">0.00</div>
                    </td>
                </tr>
            
                <tr id="tr_6" class="rowGrid0" >
                    <div id="descr_6" style="display:none"></div>
                    <td align="left">
                        <div id="accountID_6">1403</div>
                    </td>
                    <td>
                        <div id="account_6">原材料</div>
                    </td>
                    <td align="right">
                        <div id="opening_debit_6">0.00</div>
                    </td>
                    <td align="right">
                        <div id="opening_lend_6">0.00</div>
                    </td>
                    <td align="right">
                        <div id="current_debit_6">23697567.12</div>
                    </td>
                    <td align="right">
                        <div id="current_lend_6">16171894.89</div>
                    </td>
                    <td align="right">
                        <div id="endtime_debit_6">7525672.23</div>
                    </td>
                    <td align="right">
                        <div id="endtime_lend_6">0.00</div>
                    </td>
                </tr>
            
                <tr id="tr_7" class="rowGrid1" >
                    <div id="descr_7" style="display:none"></div>
                    <td align="left">
                        <div id="accountID_7">1405</div>
                    </td>
                    <td>
                        <div id="account_7">库存商品</div>
                    </td>
                    <td align="right">
                        <div id="opening_debit_7">0.00</div>
                    </td>
                    <td align="right">
                        <div id="opening_lend_7">0.00</div>
                    </td>
                    <td align="right">
                        <div id="current_debit_7">16495903.80</div>
                    </td>
                    <td align="right">
                        <div id="current_lend_7">15614259.25</div>
                    </td>
                    <td align="right">
                        <div id="endtime_debit_7">881644.55</div>
                    </td>
                    <td align="right">
                        <div id="endtime_lend_7">0.00</div>
                    </td>
                </tr>
            
                <tr id="tr_8" class="rowGrid0" >
                    <div id="descr_8" style="display:none"></div>
                    <td align="left">
                        <div id="accountID_8">1601</div>
                    </td>
                    <td>
                        <div id="account_8">固定资产</div>
                    </td>
                    <td align="right">
                        <div id="opening_debit_8">0.00</div>
                    </td>
                    <td align="right">
                        <div id="opening_lend_8">0.00</div>
                    </td>
                    <td align="right">
                        <div id="current_debit_8">72036.00</div>
                    </td>
                    <td align="right">
                        <div id="current_lend_8">0.00</div>
                    </td>
                    <td align="right">
                        <div id="endtime_debit_8">72036.00</div>
                    </td>
                    <td align="right">
                        <div id="endtime_lend_8">0.00</div>
                    </td>
                </tr>
            
                <tr id="tr_9" class="rowGrid1" >
                    <div id="descr_9" style="display:none"></div>
                    <td align="left">
                        <div id="accountID_9">1602</div>
                    </td>
                    <td>
                        <div id="account_9">累计折旧</div>
                    </td>
                    <td align="right">
                        <div id="opening_debit_9">0.00</div>
                    </td>
                    <td align="right">
                        <div id="opening_lend_9">0.00</div>
                    </td>
                    <td align="right">
                        <div id="current_debit_9">0.00</div>
                    </td>
                    <td align="right">
                        <div id="current_lend_9">1900.95</div>
                    </td>
                    <td align="right">
                        <div id="endtime_debit_9">0.00</div>
                    </td>
                    <td align="right">
                        <div id="endtime_lend_9">1900.95</div>
                    </td>
                </tr>
            
                <tr id="tr_10" class="rowGrid0" >
                    <div id="descr_10" style="display:none"></div>
                    <td align="left">
                        <div id="accountID_10">2001</div>
                    </td>
                    <td>
                        <div id="account_10">短期借款</div>
                    </td>
                    <td align="right">
                        <div id="opening_debit_10">0.00</div>
                    </td>
                    <td align="right">
                        <div id="opening_lend_10">0.00</div>
                    </td>
                    <td align="right">
                        <div id="current_debit_10">0.00</div>
                    </td>
                    <td align="right">
                        <div id="current_lend_10">5000000.00</div>
                    </td>
                    <td align="right">
                        <div id="endtime_debit_10">0.00</div>
                    </td>
                    <td align="right">
                        <div id="endtime_lend_10">5000000.00</div>
                    </td>
                </tr>
            
                <tr id="tr_11" class="rowGrid1" >
                    <div id="descr_11" style="display:none"></div>
                    <td align="left">
                        <div id="accountID_11">2202</div>
                    </td>
                    <td>
                        <div id="account_11">应付账款</div>
                    </td>
                    <td align="right">
                        <div id="opening_debit_11">0.00</div>
                    </td>
                    <td align="right">
                        <div id="opening_lend_11">0.00</div>
                    </td>
                    <td align="right">
                        <div id="current_debit_11">15362291.22</div>
                    </td>
                    <td align="right">
                        <div id="current_lend_11">27718181.94</div>
                    </td>
                    <td align="right">
                        <div id="endtime_debit_11">0.00</div>
                    </td>
                    <td align="right">
                        <div id="endtime_lend_11">12355890.72</div>
                    </td>
                </tr>
            
                <tr id="tr_12" class="rowGrid0" >
                    <div id="descr_12" style="display:none"></div>
                    <td align="left">
                        <div id="accountID_12">2211</div>
                    </td>
                    <td>
                        <div id="account_12">应付职工薪酬</div>
                    </td>
                    <td align="right">
                        <div id="opening_debit_12">0.00</div>
                    </td>
                    <td align="right">
                        <div id="opening_lend_12">0.00</div>
                    </td>
                    <td align="right">
                        <div id="current_debit_12">0.00</div>
                    </td>
                    <td align="right">
                        <div id="current_lend_12">2592909.44</div>
                    </td>
                    <td align="right">
                        <div id="endtime_debit_12">0.00</div>
                    </td>
                    <td align="right">
                        <div id="endtime_lend_12">2592909.44</div>
                    </td>
                </tr>
            
                <tr id="tr_13" class="rowGrid1" >
                    <div id="descr_13" style="display:none"></div>
                    <td align="left">
                        <div id="accountID_13">2221</div>
                    </td>
                    <td>
                        <div id="account_13">应交税费</div>
                    </td>
                    <td align="right">
                        <div id="opening_debit_13">0.00</div>
                    </td>
                    <td align="right">
                        <div id="opening_lend_13">0.00</div>
                    </td>
                    <td align="right">
                        <div id="current_debit_13">4614147.91</div>
                    </td>
                    <td align="right">
                        <div id="current_lend_13">3025090.33</div>
                    </td>
                    <td align="right">
                        <div id="endtime_debit_13">1589057.58</div>
                    </td>
                    <td align="right">
                        <div id="endtime_lend_13">0.00</div>
                    </td>
                </tr>
            
                <tr id="tr_14" class="rowGrid0" >
                    <div id="descr_14" style="display:none"></div>
                    <td align="left">
                        <div id="accountID_14">2801</div>
                    </td>
                    <td>
                        <div id="account_14">预计负债</div>
                    </td>
                    <td align="right">
                        <div id="opening_debit_14">0.00</div>
                    </td>
                    <td align="right">
                        <div id="opening_lend_14">0.00</div>
                    </td>
                    <td align="right">
                        <div id="current_debit_14">0.00</div>
                    </td>
                    <td align="right">
                        <div id="current_lend_14">622812.72</div>
                    </td>
                    <td align="right">
                        <div id="endtime_debit_14">0.00</div>
                    </td>
                    <td align="right">
                        <div id="endtime_lend_14">622812.72</div>
                    </td>
                </tr>
            
                <tr id="tr_15" class="rowGrid1" >
                    <div id="descr_15" style="display:none"></div>
                    <td align="left">
                        <div id="accountID_15">4001</div>
                    </td>
                    <td>
                        <div id="account_15">实收资本</div>
                    </td>
                    <td align="right">
                        <div id="opening_debit_15">0.00</div>
                    </td>
                    <td align="right">
                        <div id="opening_lend_15">0.00</div>
                    </td>
                    <td align="right">
                        <div id="current_debit_15">0.00</div>
                    </td>
                    <td align="right">
                        <div id="current_lend_15">5000000.00</div>
                    </td>
                    <td align="right">
                        <div id="endtime_debit_15">0.00</div>
                    </td>
                    <td align="right">
                        <div id="endtime_lend_15">5000000.00</div>
                    </td>
                </tr>
            
                <tr id="tr_16" class="rowGrid0" >
                    <div id="descr_16" style="display:none"></div>
                    <td align="left">
                        <div id="accountID_16">4103</div>
                    </td>
                    <td>
                        <div id="account_16">本年利润</div>
                    </td>
                    <td align="right">
                        <div id="opening_debit_16">0.00</div>
                    </td>
                    <td align="right">
                        <div id="opening_lend_16">0.00</div>
                    </td>
                    <td align="right">
                        <div id="current_debit_16">18695656.46</div>
                    </td>
                    <td align="right">
                        <div id="current_lend_16">18032463.19</div>
                    </td>
                    <td align="right">
                        <div id="endtime_debit_16">663193.27</div>
                    </td>
                    <td align="right">
                        <div id="endtime_lend_16">0.00</div>
                    </td>
                </tr>
            
                <tr id="tr_17" class="rowGrid1" >
                    <div id="descr_17" style="display:none"></div>
                    <td align="left">
                        <div id="accountID_17">5001</div>
                    </td>
                    <td>
                        <div id="account_17">生产成本</div>
                    </td>
                    <td align="right">
                        <div id="opening_debit_17">0.00</div>
                    </td>
                    <td align="right">
                        <div id="opening_lend_17">0.00</div>
                    </td>
                    <td align="right">
                        <div id="current_debit_17">19323228.39</div>
                    </td>
                    <td align="right">
                        <div id="current_lend_17">16495903.80</div>
                    </td>
                    <td align="right">
                        <div id="endtime_debit_17">2827324.59</div>
                    </td>
                    <td align="right">
                        <div id="endtime_lend_17">0.00</div>
                    </td>
                </tr>
            
                <tr id="tr_18" class="rowGrid0" >
                    <div id="descr_18" style="display:none"></div>
                    <td align="left">
                        <div id="accountID_18">5101</div>
                    </td>
                    <td>
                        <div id="account_18">制造费用</div>
                    </td>
                    <td align="right">
                        <div id="opening_debit_18">0.00</div>
                    </td>
                    <td align="right">
                        <div id="opening_lend_18">0.00</div>
                    </td>
                    <td align="right">
                        <div id="current_debit_18">261096.91</div>
                    </td>
                    <td align="right">
                        <div id="current_lend_18">261096.91</div>
                    </td>
                    <td align="right">
                        <div id="endtime_debit_18">0.00</div>
                    </td>
                    <td align="right">
                        <div id="endtime_lend_18">0.00</div>
                    </td>
                </tr>
            
                <tr id="tr_19" class="rowGrid1" >
                    <div id="descr_19" style="display:none"></div>
                    <td align="left">
                        <div id="accountID_19">6001</div>
                    </td>
                    <td>
                        <div id="account_19">主营业务收入</div>
                    </td>
                    <td align="right">
                        <div id="opening_debit_19">0.00</div>
                    </td>
                    <td align="right">
                        <div id="opening_lend_19">0.00</div>
                    </td>
                    <td align="right">
                        <div id="current_debit_19">17794649.00</div>
                    </td>
                    <td align="right">
                        <div id="current_lend_19">17794649.00</div>
                    </td>
                    <td align="right">
                        <div id="endtime_debit_19">0.00</div>
                    </td>
                    <td align="right">
                        <div id="endtime_lend_19">0.00</div>
                    </td>
                </tr>
            
                <tr id="tr_20" class="rowGrid0" >
                    <div id="descr_20" style="display:none"></div>
                    <td align="left">
                        <div id="accountID_20">6101</div>
                    </td>
                    <td>
                        <div id="account_20">公允价值变动损益</div>
                    </td>
                    <td align="right">
                        <div id="opening_debit_20">0.00</div>
                    </td>
                    <td align="right">
                        <div id="opening_lend_20">0.00</div>
                    </td>
                    <td align="right">
                        <div id="current_debit_20">38.00</div>
                    </td>
                    <td align="right">
                        <div id="current_lend_20">38.00</div>
                    </td>
                    <td align="right">
                        <div id="endtime_debit_20">0.00</div>
                    </td>
                    <td align="right">
                        <div id="endtime_lend_20">0.00</div>
                    </td>
                </tr>
            
                <tr id="tr_21" class="rowGrid1" >
                    <div id="descr_21" style="display:none"></div>
                    <td align="left">
                        <div id="accountID_21">6111</div>
                    </td>
                    <td>
                        <div id="account_21">投资收益</div>
                    </td>
                    <td align="right">
                        <div id="opening_debit_21">0.00</div>
                    </td>
                    <td align="right">
                        <div id="opening_lend_21">0.00</div>
                    </td>
                    <td align="right">
                        <div id="current_debit_21">0.68</div>
                    </td>
                    <td align="right">
                        <div id="current_lend_21">0.68</div>
                    </td>
                    <td align="right">
                        <div id="endtime_debit_21">0.00</div>
                    </td>
                    <td align="right">
                        <div id="endtime_lend_21">0.00</div>
                    </td>
                </tr>
            
                <tr id="tr_22" class="rowGrid0" >
                    <div id="descr_22" style="display:none"></div>
                    <td align="left">
                        <div id="accountID_22">6401</div>
                    </td>
                    <td>
                        <div id="account_22">主营业务成本</div>
                    </td>
                    <td align="right">
                        <div id="opening_debit_22">0.00</div>
                    </td>
                    <td align="right">
                        <div id="opening_lend_22">0.00</div>
                    </td>
                    <td align="right">
                        <div id="current_debit_22">15614259.25</div>
                    </td>
                    <td align="right">
                        <div id="current_lend_22">15614259.25</div>
                    </td>
                    <td align="right">
                        <div id="endtime_debit_22">0.00</div>
                    </td>
                    <td align="right">
                        <div id="endtime_lend_22">0.00</div>
                    </td>
                </tr>
            
                <tr id="tr_23" class="rowGrid1" >
                    <div id="descr_23" style="display:none"></div>
                    <td align="left">
                        <div id="accountID_23">6601</div>
                    </td>
                    <td>
                        <div id="account_23">销售费用</div>
                    </td>
                    <td align="right">
                        <div id="opening_debit_23">0.00</div>
                    </td>
                    <td align="right">
                        <div id="opening_lend_23">0.00</div>
                    </td>
                    <td align="right">
                        <div id="current_debit_23">2995613.31</div>
                    </td>
                    <td align="right">
                        <div id="current_lend_23">2995613.31</div>
                    </td>
                    <td align="right">
                        <div id="endtime_debit_23">0.00</div>
                    </td>
                    <td align="right">
                        <div id="endtime_lend_23">0.00</div>
                    </td>
                </tr>
            
                <tr id="tr_24" class="rowGrid0" >
                    <div id="descr_24" style="display:none"></div>
                    <td align="left">
                        <div id="accountID_24">6602</div>
                    </td>
                    <td>
                        <div id="account_24">管理费用</div>
                    </td>
                    <td align="right">
                        <div id="opening_debit_24">0.00</div>
                    </td>
                    <td align="right">
                        <div id="opening_lend_24">0.00</div>
                    </td>
                    <td align="right">
                        <div id="current_debit_24">85583.22</div>
                    </td>
                    <td align="right">
                        <div id="current_lend_24">85583.22</div>
                    </td>
                    <td align="right">
                        <div id="endtime_debit_24">0.00</div>
                    </td>
                    <td align="right">
                        <div id="endtime_lend_24">0.00</div>
                    </td>
                </tr>
            
                <tr id="tr_25" class="rowGrid1" >
                    <div id="descr_25" style="display:none"></div>
                    <td align="left">
                        <div id="accountID_25">6603</div>
                    </td>
                    <td>
                        <div id="account_25">财务费用</div>
                    </td>
                    <td align="right">
                        <div id="opening_debit_25">0.00</div>
                    </td>
                    <td align="right">
                        <div id="opening_lend_25">0.00</div>
                    </td>
                    <td align="right">
                        <div id="current_debit_25">237652.19</div>
                    </td>
                    <td align="right">
                        <div id="current_lend_25">237652.19</div>
                    </td>
                    <td align="right">
                        <div id="endtime_debit_25">0.00</div>
                    </td>
                    <td align="right">
                        <div id="endtime_lend_25">0.00</div>
                    </td>
                </tr>
            
            <tr>
                <td></td>
                <td>合计</td>
                <td align="right">
                    <div id="opening_debit_amount">0.00</div>
                </td>
                <td align="right">
                    <div id="opening_lend_amount">0.00</div>
                </td>
                <td align="right">
                    <div id="current_debit_amount">168248515.98</div>
                </td>
                <td align="right">
                    <div id="current_lend_amount">168248515.98</div>
                </td>
                <td align="right">
                    <div id="endtime_debit_amount">25573513.83</div>
                </td>
                <td align="right">
                    <div id="endtime_lend_amount">25573513.83</div>
                </td>
            </tr>
        
        <tr class="tableGridFooter">
            <td colspan="20">
                <table style="width:100%" class="tableNoLine">
                    <tr class="tableGridFooter">
                        <td align="left">
                        </td>
                        <td align="right">
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</div>
</body>
</html>
<script>
//刷新窗口
function doRefreshPage(){
    location.href="do?mm=10&start=trial_balance_statement&action=dsh/dsh_statement&yyyy=2016";
}
</script>
<script language="JavaScript" type="text/javascript">
$(document).ready(function(){
    $("#yyyy").val("2016");
    $("#mm").val("10");
});
</script>

'''

html11 = '''
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">








<html>
<head>
<title>试算平衡表</title>


<link href="css/blue_text.css" rel="stylesheet" type="text/css">
<link href="css/netinnet_css.css" rel="stylesheet" type="text/css">
<link href="css/softkf_common.css" rel="stylesheet" type="text/css">




<script>
    var _loginRole = 'M';   //login role
    var _sysRoleContral = '1';    //role contral
    var _sysTalkIM = '0'; //IM contral
    var _sysDecision = '1'; //??×÷????????
    var _bankruptcy = '0'
</script>
<script language="JavaScript" src="javascript/basic.js"></script>
<script language="JavaScript" src="javascript/operation.js"></script>
<script language="JavaScript" src="javascript/encoder.js"></script>
<script language="JavaScript" src="javascript/checkForm.js"></script>
<script language="JavaScript" src="javascript/jquery-1.6.1.min.js"></script>
<script language="JavaScript" src="javascript/dateSelect.js"></script>
<script type="text/javascript" src="javascript/multiTags.js"></script>
<script type="text/javascript" src="javascript/workStatus.js"></script>
<script language="JavaScript" src="javascript/softkf_common.js"></script>
<script language="JavaScript" src="javascript/MyQuickSelect.js"></script>
<script language="JavaScript" src="javascript/UrlManager.js"></script>
<script language="JavaScript" src="javascript/sandtable.js"></script>
<script language="JavaScript" src="javascript/loadmask/jquery.loadmask.js"></script>
<!-- 20150525 panyp add -->
<script language="JavaScript" src="javascript/browser.js?p=p"></script>
<link href="javascript/loadmask/jquery.loadmask.css" rel="stylesheet" type="text/css" />

<script language="JavaScript">
document.ondblclick=function(e){
    return false;
}
</script>

</head>
<body>
<div class="common_contentDiv">
    <form name="common_query" action="do" method="post" >
    <input type="hidden" name="action" value="dsh/dsh_statement" />
    <input id="start" type="hidden" name="start" value="trial_balance_statement" />
    <table class="tableNoLine" >
        <tr>
            <td align="left"><span class="titlePage">【试算平衡表】</span></td>
            <td align="right" nowrap="nowrap">年份:</td>
            <td>
                <select id="yyyy" name="yyyy" class="selectList">
                  <option value="" selected></option>
                  
                        <option value="2016">2016</option>
                    
                        <option value="2017">2017</option>
                    
                  
                </select>
            </td>
            <td align="right" nowrap="nowrap">月份:</td>
            <td>
                <select id="mm" name="mm" class="selectList">
                    <option value="" selected></option> 
                  
                    <option value="1">1</option>
                  
                    <option value="2">2</option>
                  
                    <option value="3">3</option>
                  
                    <option value="4">4</option>
                  
                    <option value="5">5</option>
                  
                    <option value="6">6</option>
                  
                    <option value="7">7</option>
                  
                    <option value="8">8</option>
                  
                    <option value="9">9</option>
                  
                    <option value="10">10</option>
                  
                    <option value="11">11</option>
                  
                    <option value="12">12</option>
                   
                </select>
            </td>
            <td align="right">
                <input id="btn_query" type="button" class="btnSubmit" value="查询" onclick="common_query.submit();" />
            </td>
        </tr>
    </table>
    </form>
    <table style="width:100%" class="tableGrid" border="1">
        <tr class="tableGridHeader" align="center">
            <td width="25%" colspan="2">科目</td>
            <td width="20%" colspan="2">期初余额</td>
            <td width="20%" colspan="2">本期发生额</td>
            <td width="20%" colspan="2">期末余额</td>
        </tr>
        <tr class="tableGridHeader" align="center">
            <td width="10%">代码</td>
            <td width="15%">名称</td>
            <td width="10%">借方</td>
            <td width="10%">贷方</td>
            <td width="10%">借方</td>
            <td width="10%">贷方</td>
            <td width="10%">借方</td>
            <td width="10%">贷方</td>
        </tr>
        
                <tr id="tr_1" class="rowGrid1" >
                    <div id="descr_1" style="display:none"></div>
                    <td align="left">
                        <div id="accountID_1">1001</div>
                    </td>
                    <td>
                        <div id="account_1">库存现金</div>
                    </td>
                    <td align="right">
                        <div id="opening_debit_1">36280.09</div>
                    </td>
                    <td align="right">
                        <div id="opening_lend_1">0.00</div>
                    </td>
                    <td align="right">
                        <div id="current_debit_1">50000.00</div>
                    </td>
                    <td align="right">
                        <div id="current_lend_1">60081.89</div>
                    </td>
                    <td align="right">
                        <div id="endtime_debit_1">26198.20</div>
                    </td>
                    <td align="right">
                        <div id="endtime_lend_1">0.00</div>
                    </td>
                </tr>
            
                <tr id="tr_2" class="rowGrid0" >
                    <div id="descr_2" style="display:none"></div>
                    <td align="left">
                        <div id="accountID_2">1002</div>
                    </td>
                    <td>
                        <div id="account_2">银行存款</div>
                    </td>
                    <td align="right">
                        <div id="opening_debit_2">2580042.85</div>
                    </td>
                    <td align="right">
                        <div id="opening_lend_2">0.00</div>
                    </td>
                    <td align="right">
                        <div id="current_debit_2">36279666.44</div>
                    </td>
                    <td align="right">
                        <div id="current_lend_2">35377235.78</div>
                    </td>
                    <td align="right">
                        <div id="endtime_debit_2">3482473.51</div>
                    </td>
                    <td align="right">
                        <div id="endtime_lend_2">0.00</div>
                    </td>
                </tr>
            
                <tr id="tr_3" class="rowGrid1" >
                    <div id="descr_3" style="display:none"></div>
                    <td align="left">
                        <div id="accountID_3">1101</div>
                    </td>
                    <td>
                        <div id="account_3">交易性金融资产</div>
                    </td>
                    <td align="right">
                        <div id="opening_debit_3">642.00</div>
                    </td>
                    <td align="right">
                        <div id="opening_lend_3">0.00</div>
                    </td>
                    <td align="right">
                        <div id="current_debit_3">38.00</div>
                    </td>
                    <td align="right">
                        <div id="current_lend_3">680.00</div>
                    </td>
                    <td align="right">
                        <div id="endtime_debit_3">0.00</div>
                    </td>
                    <td align="right">
                        <div id="endtime_lend_3">0.00</div>
                    </td>
                </tr>
            
                <tr id="tr_4" class="rowGrid0" >
                    <div id="descr_4" style="display:none"></div>
                    <td align="left">
                        <div id="accountID_4">1122</div>
                    </td>
                    <td>
                        <div id="account_4">应收账款</div>
                    </td>
                    <td align="right">
                        <div id="opening_debit_4">7319571.48</div>
                    </td>
                    <td align="right">
                        <div id="opening_lend_4">0.00</div>
                    </td>
                    <td align="right">
                        <div id="current_debit_4">4936173.84</div>
                    </td>
                    <td align="right">
                        <div id="current_lend_4">7319571.48</div>
                    </td>
                    <td align="right">
                        <div id="endtime_debit_4">4936173.84</div>
                    </td>
                    <td align="right">
                        <div id="endtime_lend_4">0.00</div>
                    </td>
                </tr>
            
                <tr id="tr_5" class="rowGrid1" >
                    <div id="descr_5" style="display:none"></div>
                    <td align="left">
                        <div id="accountID_5">1221</div>
                    </td>
                    <td>
                        <div id="account_5">其他应收款</div>
                    </td>
                    <td align="right">
                        <div id="opening_debit_5">2078049.19</div>
                    </td>
                    <td align="right">
                        <div id="opening_lend_5">0.00</div>
                    </td>
                    <td align="right">
                        <div id="current_debit_5">0.00</div>
                    </td>
                    <td align="right">
                        <div id="current_lend_5">692683.08</div>
                    </td>
                    <td align="right">
                        <div id="endtime_debit_5">1385366.11</div>
                    </td>
                    <td align="right">
                        <div id="endtime_lend_5">0.00</div>
                    </td>
                </tr>
            
                <tr id="tr_6" class="rowGrid0" >
                    <div id="descr_6" style="display:none"></div>
                    <td align="left">
                        <div id="accountID_6">1403</div>
                    </td>
                    <td>
                        <div id="account_6">原材料</div>
                    </td>
                    <td align="right">
                        <div id="opening_debit_6">7525672.23</div>
                    </td>
                    <td align="right">
                        <div id="opening_lend_6">0.00</div>
                    </td>
                    <td align="right">
                        <div id="current_debit_6">29066953.89</div>
                    </td>
                    <td align="right">
                        <div id="current_lend_6">21342977.98</div>
                    </td>
                    <td align="right">
                        <div id="endtime_debit_6">15249648.14</div>
                    </td>
                    <td align="right">
                        <div id="endtime_lend_6">0.00</div>
                    </td>
                </tr>
            
                <tr id="tr_7" class="rowGrid1" >
                    <div id="descr_7" style="display:none"></div>
                    <td align="left">
                        <div id="accountID_7">1405</div>
                    </td>
                    <td>
                        <div id="account_7">库存商品</div>
                    </td>
                    <td align="right">
                        <div id="opening_debit_7">881644.55</div>
                    </td>
                    <td align="right">
                        <div id="opening_lend_7">0.00</div>
                    </td>
                    <td align="right">
                        <div id="current_debit_7">24368851.03</div>
                    </td>
                    <td align="right">
                        <div id="current_lend_7">23776725.85</div>
                    </td>
                    <td align="right">
                        <div id="endtime_debit_7">1473769.73</div>
                    </td>
                    <td align="right">
                        <div id="endtime_lend_7">0.00</div>
                    </td>
                </tr>
            
                <tr id="tr_8" class="rowGrid0" >
                    <div id="descr_8" style="display:none"></div>
                    <td align="left">
                        <div id="accountID_8">1601</div>
                    </td>
                    <td>
                        <div id="account_8">固定资产</div>
                    </td>
                    <td align="right">
                        <div id="opening_debit_8">72036.00</div>
                    </td>
                    <td align="right">
                        <div id="opening_lend_8">0.00</div>
                    </td>
                    <td align="right">
                        <div id="current_debit_8">0.00</div>
                    </td>
                    <td align="right">
                        <div id="current_lend_8">0.00</div>
                    </td>
                    <td align="right">
                        <div id="endtime_debit_8">72036.00</div>
                    </td>
                    <td align="right">
                        <div id="endtime_lend_8">0.00</div>
                    </td>
                </tr>
            
                <tr id="tr_9" class="rowGrid1" >
                    <div id="descr_9" style="display:none"></div>
                    <td align="left">
                        <div id="accountID_9">1602</div>
                    </td>
                    <td>
                        <div id="account_9">累计折旧</div>
                    </td>
                    <td align="right">
                        <div id="opening_debit_9">0.00</div>
                    </td>
                    <td align="right">
                        <div id="opening_lend_9">1900.95</div>
                    </td>
                    <td align="right">
                        <div id="current_debit_9">0.00</div>
                    </td>
                    <td align="right">
                        <div id="current_lend_9">1900.95</div>
                    </td>
                    <td align="right">
                        <div id="endtime_debit_9">0.00</div>
                    </td>
                    <td align="right">
                        <div id="endtime_lend_9">3801.90</div>
                    </td>
                </tr>
            
                <tr id="tr_10" class="rowGrid0" >
                    <div id="descr_10" style="display:none"></div>
                    <td align="left">
                        <div id="accountID_10">2001</div>
                    </td>
                    <td>
                        <div id="account_10">短期借款</div>
                    </td>
                    <td align="right">
                        <div id="opening_debit_10">0.00</div>
                    </td>
                    <td align="right">
                        <div id="opening_lend_10">5000000.00</div>
                    </td>
                    <td align="right">
                        <div id="current_debit_10">0.00</div>
                    </td>
                    <td align="right">
                        <div id="current_lend_10">0.00</div>
                    </td>
                    <td align="right">
                        <div id="endtime_debit_10">0.00</div>
                    </td>
                    <td align="right">
                        <div id="endtime_lend_10">5000000.00</div>
                    </td>
                </tr>
            
                <tr id="tr_11" class="rowGrid1" >
                    <div id="descr_11" style="display:none"></div>
                    <td align="left">
                        <div id="accountID_11">2202</div>
                    </td>
                    <td>
                        <div id="account_11">应付账款</div>
                    </td>
                    <td align="right">
                        <div id="opening_debit_11">0.00</div>
                    </td>
                    <td align="right">
                        <div id="opening_lend_11">12355890.72</div>
                    </td>
                    <td align="right">
                        <div id="current_debit_11">32417387.81</div>
                    </td>
                    <td align="right">
                        <div id="current_lend_11">33999595.60</div>
                    </td>
                    <td align="right">
                        <div id="endtime_debit_11">0.00</div>
                    </td>
                    <td align="right">
                        <div id="endtime_lend_11">13938098.51</div>
                    </td>
                </tr>
            
                <tr id="tr_12" class="rowGrid0" >
                    <div id="descr_12" style="display:none"></div>
                    <td align="left">
                        <div id="accountID_12">2211</div>
                    </td>
                    <td>
                        <div id="account_12">应付职工薪酬</div>
                    </td>
                    <td align="right">
                        <div id="opening_debit_12">0.00</div>
                    </td>
                    <td align="right">
                        <div id="opening_lend_12">2592909.44</div>
                    </td>
                    <td align="right">
                        <div id="current_debit_12">2592909.44</div>
                    </td>
                    <td align="right">
                        <div id="current_lend_12">2743020.55</div>
                    </td>
                    <td align="right">
                        <div id="endtime_debit_12">0.00</div>
                    </td>
                    <td align="right">
                        <div id="endtime_lend_12">2743020.55</div>
                    </td>
                </tr>
            
                <tr id="tr_13" class="rowGrid1" >
                    <div id="descr_13" style="display:none"></div>
                    <td align="left">
                        <div id="accountID_13">2221</div>
                    </td>
                    <td>
                        <div id="account_13">应交税费</div>
                    </td>
                    <td align="right">
                        <div id="opening_debit_13">1589057.58</div>
                    </td>
                    <td align="right">
                        <div id="opening_lend_13">0.00</div>
                    </td>
                    <td align="right">
                        <div id="current_debit_13">4981713.92</div>
                    </td>
                    <td align="right">
                        <div id="current_lend_13">4946520.71</div>
                    </td>
                    <td align="right">
                        <div id="endtime_debit_13">1624250.79</div>
                    </td>
                    <td align="right">
                        <div id="endtime_lend_13">0.00</div>
                    </td>
                </tr>
            
                <tr id="tr_14" class="rowGrid0" >
                    <div id="descr_14" style="display:none"></div>
                    <td align="left">
                        <div id="accountID_14">2801</div>
                    </td>
                    <td>
                        <div id="account_14">预计负债</div>
                    </td>
                    <td align="right">
                        <div id="opening_debit_14">0.00</div>
                    </td>
                    <td align="right">
                        <div id="opening_lend_14">622812.72</div>
                    </td>
                    <td align="right">
                        <div id="current_debit_14">0.00</div>
                    </td>
                    <td align="right">
                        <div id="current_lend_14">724266.05</div>
                    </td>
                    <td align="right">
                        <div id="endtime_debit_14">0.00</div>
                    </td>
                    <td align="right">
                        <div id="endtime_lend_14">1347078.77</div>
                    </td>
                </tr>
            
                <tr id="tr_15" class="rowGrid1" >
                    <div id="descr_15" style="display:none"></div>
                    <td align="left">
                        <div id="accountID_15">4001</div>
                    </td>
                    <td>
                        <div id="account_15">实收资本</div>
                    </td>
                    <td align="right">
                        <div id="opening_debit_15">0.00</div>
                    </td>
                    <td align="right">
                        <div id="opening_lend_15">5000000.00</div>
                    </td>
                    <td align="right">
                        <div id="current_debit_15">0.00</div>
                    </td>
                    <td align="right">
                        <div id="current_lend_15">0.00</div>
                    </td>
                    <td align="right">
                        <div id="endtime_debit_15">0.00</div>
                    </td>
                    <td align="right">
                        <div id="endtime_lend_15">5000000.00</div>
                    </td>
                </tr>
            
                <tr id="tr_16" class="rowGrid0" >
                    <div id="descr_16" style="display:none"></div>
                    <td align="left">
                        <div id="accountID_16">4103</div>
                    </td>
                    <td>
                        <div id="account_16">本年利润</div>
                    </td>
                    <td align="right">
                        <div id="opening_debit_16">663193.27</div>
                    </td>
                    <td align="right">
                        <div id="opening_lend_16">0.00</div>
                    </td>
                    <td align="right">
                        <div id="current_debit_16">25354231.07</div>
                    </td>
                    <td align="right">
                        <div id="current_lend_16">29252262.35</div>
                    </td>
                    <td align="right">
                        <div id="endtime_debit_16">0.00</div>
                    </td>
                    <td align="right">
                        <div id="endtime_lend_16">3234838.01</div>
                    </td>
                </tr>
            
                <tr id="tr_17" class="rowGrid1" >
                    <div id="descr_17" style="display:none"></div>
                    <td align="left">
                        <div id="accountID_17">5001</div>
                    </td>
                    <td>
                        <div id="account_17">生产成本</div>
                    </td>
                    <td align="right">
                        <div id="opening_debit_17">2827324.59</div>
                    </td>
                    <td align="right">
                        <div id="opening_lend_17">0.00</div>
                    </td>
                    <td align="right">
                        <div id="current_debit_17">24558447.86</div>
                    </td>
                    <td align="right">
                        <div id="current_lend_17">24368851.03</div>
                    </td>
                    <td align="right">
                        <div id="endtime_debit_17">3016921.42</div>
                    </td>
                    <td align="right">
                        <div id="endtime_lend_17">0.00</div>
                    </td>
                </tr>
            
                <tr id="tr_18" class="rowGrid0" >
                    <div id="descr_18" style="display:none"></div>
                    <td align="left">
                        <div id="accountID_18">5101</div>
                    </td>
                    <td>
                        <div id="account_18">制造费用</div>
                    </td>
                    <td align="right">
                        <div id="opening_debit_18">0.00</div>
                    </td>
                    <td align="right">
                        <div id="opening_lend_18">0.00</div>
                    </td>
                    <td align="right">
                        <div id="current_debit_18">325233.29</div>
                    </td>
                    <td align="right">
                        <div id="current_lend_18">325233.29</div>
                    </td>
                    <td align="right">
                        <div id="endtime_debit_18">0.00</div>
                    </td>
                    <td align="right">
                        <div id="endtime_lend_18">0.00</div>
                    </td>
                </tr>
            
                <tr id="tr_19" class="rowGrid1" >
                    <div id="descr_19" style="display:none"></div>
                    <td align="left">
                        <div id="accountID_19">6001</div>
                    </td>
                    <td>
                        <div id="account_19">主营业务收入</div>
                    </td>
                    <td align="right">
                        <div id="opening_debit_19">0.00</div>
                    </td>
                    <td align="right">
                        <div id="opening_lend_19">0.00</div>
                    </td>
                    <td align="right">
                        <div id="current_debit_19">28970642.00</div>
                    </td>
                    <td align="right">
                        <div id="current_lend_19">28970642.00</div>
                    </td>
                    <td align="right">
                        <div id="endtime_debit_19">0.00</div>
                    </td>
                    <td align="right">
                        <div id="endtime_lend_19">0.00</div>
                    </td>
                </tr>
            
                <tr id="tr_20" class="rowGrid0" >
                    <div id="descr_20" style="display:none"></div>
                    <td align="left">
                        <div id="accountID_20">6101</div>
                    </td>
                    <td>
                        <div id="account_20">公允价值变动损益</div>
                    </td>
                    <td align="right">
                        <div id="opening_debit_20">0.00</div>
                    </td>
                    <td align="right">
                        <div id="opening_lend_20">0.00</div>
                    </td>
                    <td align="right">
                        <div id="current_debit_20">38.00</div>
                    </td>
                    <td align="right">
                        <div id="current_lend_20">38.00</div>
                    </td>
                    <td align="right">
                        <div id="endtime_debit_20">0.00</div>
                    </td>
                    <td align="right">
                        <div id="endtime_lend_20">0.00</div>
                    </td>
                </tr>
            
                <tr id="tr_21" class="rowGrid1" >
                    <div id="descr_21" style="display:none"></div>
                    <td align="left">
                        <div id="accountID_21">6111</div>
                    </td>
                    <td>
                        <div id="account_21">投资收益</div>
                    </td>
                    <td align="right">
                        <div id="opening_debit_21">0.00</div>
                    </td>
                    <td align="right">
                        <div id="opening_lend_21">0.00</div>
                    </td>
                    <td align="right">
                        <div id="current_debit_21">62.34</div>
                    </td>
                    <td align="right">
                        <div id="current_lend_21">62.34</div>
                    </td>
                    <td align="right">
                        <div id="endtime_debit_21">0.00</div>
                    </td>
                    <td align="right">
                        <div id="endtime_lend_21">0.00</div>
                    </td>
                </tr>
            
                <tr id="tr_22" class="rowGrid0" >
                    <div id="descr_22" style="display:none"></div>
                    <td align="left">
                        <div id="accountID_22">6401</div>
                    </td>
                    <td>
                        <div id="account_22">主营业务成本</div>
                    </td>
                    <td align="right">
                        <div id="opening_debit_22">0.00</div>
                    </td>
                    <td align="right">
                        <div id="opening_lend_22">0.00</div>
                    </td>
                    <td align="right">
                        <div id="current_debit_22">23776725.85</div>
                    </td>
                    <td align="right">
                        <div id="current_lend_22">23776725.85</div>
                    </td>
                    <td align="right">
                        <div id="endtime_debit_22">0.00</div>
                    </td>
                    <td align="right">
                        <div id="endtime_lend_22">0.00</div>
                    </td>
                </tr>
            
                <tr id="tr_23" class="rowGrid1" >
                    <div id="descr_23" style="display:none"></div>
                    <td align="left">
                        <div id="accountID_23">6601</div>
                    </td>
                    <td>
                        <div id="account_23">销售费用</div>
                    </td>
                    <td align="right">
                        <div id="opening_debit_23">0.00</div>
                    </td>
                    <td align="right">
                        <div id="opening_lend_23">0.00</div>
                    </td>
                    <td align="right">
                        <div id="current_debit_23">1399822.64</div>
                    </td>
                    <td align="right">
                        <div id="current_lend_23">1399822.64</div>
                    </td>
                    <td align="right">
                        <div id="endtime_debit_23">0.00</div>
                    </td>
                    <td align="right">
                        <div id="endtime_lend_23">0.00</div>
                    </td>
                </tr>
            
                <tr id="tr_24" class="rowGrid0" >
                    <div id="descr_24" style="display:none"></div>
                    <td align="left">
                        <div id="accountID_24">6602</div>
                    </td>
                    <td>
                        <div id="account_24">管理费用</div>
                    </td>
                    <td align="right">
                        <div id="opening_debit_24">0.00</div>
                    </td>
                    <td align="right">
                        <div id="opening_lend_24">0.00</div>
                    </td>
                    <td align="right">
                        <div id="current_debit_24">141016.57</div>
                    </td>
                    <td align="right">
                        <div id="current_lend_24">141016.57</div>
                    </td>
                    <td align="right">
                        <div id="endtime_debit_24">0.00</div>
                    </td>
                    <td align="right">
                        <div id="endtime_lend_24">0.00</div>
                    </td>
                </tr>
            
                <tr id="tr_25" class="rowGrid1" >
                    <div id="descr_25" style="display:none"></div>
                    <td align="left">
                        <div id="accountID_25">6603</div>
                    </td>
                    <td>
                        <div id="account_25">财务费用</div>
                    </td>
                    <td align="right">
                        <div id="opening_debit_25">0.00</div>
                    </td>
                    <td align="right">
                        <div id="opening_lend_25">0.00</div>
                    </td>
                    <td align="right">
                        <div id="current_debit_25">244978.68</div>
                    </td>
                    <td align="right">
                        <div id="current_lend_25">244978.68</div>
                    </td>
                    <td align="right">
                        <div id="endtime_debit_25">0.00</div>
                    </td>
                    <td align="right">
                        <div id="endtime_lend_25">0.00</div>
                    </td>
                </tr>
            
            <tr>
                <td></td>
                <td>合计</td>
                <td align="right">
                    <div id="opening_debit_amount">25573513.83</div>
                </td>
                <td align="right">
                    <div id="opening_lend_amount">25573513.83</div>
                </td>
                <td align="right">
                    <div id="current_debit_amount">239538100.01</div>
                </td>
                <td align="right">
                    <div id="current_lend_amount">239538100.01</div>
                </td>
                <td align="right">
                    <div id="endtime_debit_amount">31266837.74</div>
                </td>
                <td align="right">
                    <div id="endtime_lend_amount">31266837.74</div>
                </td>
            </tr>
        
        <tr class="tableGridFooter">
            <td colspan="20">
                <table style="width:100%" class="tableNoLine">
                    <tr class="tableGridFooter">
                        <td align="left">
                        </td>
                        <td align="right">
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</div>
</body>
</html>
<script>
//刷新窗口
function doRefreshPage(){
    location.href="do?mm=11&start=trial_balance_statement&action=dsh/dsh_statement&yyyy=2016";
}
</script>
<script language="JavaScript" type="text/javascript">
$(document).ready(function(){
    $("#yyyy").val("2016");
    $("#mm").val("11");
});
</script>

'''

class WZW(object):

    def __init__(self, text, rows):
        self.num = 1
        self.rows = rows
        self.bsObj = BeautifulSoup(text, "html.parser")
        self.accountID = []
        self.account = []
        self.opening_debit = []
        self.opening_lend = []
        self.current_debit = []
        self.current_lend = []
        self.endtime_debit = []
        self.endtime_lend = []
        self.accountDict = {}
        self.mark = [0,]*8
        self.mark1 = [0, 3, 1, 0, 0, 10, 0, 10]
        self.mark2 = [8, 5, 1, 2, 10, 10, 0, 10]
        self.value1 = [0.0011, 1.1975, 17189559.30, 1.0036, 0.0005, 0.4943, 0.5989, 4.5821]
        self.setupDict()
        self.setupDatas()

    def calSumOfIDList(self, IDList, accountDict, index):
        """
        index = 1 : opening_debit 借方期初
        index = 2 : opening_lend 贷方期初
        index = 3 : current_debit 借方发生额
        index = 4 : current_lend 贷方发生额
        index = 5 : endtime_debit 借方期末
        index = 6 : endtime_lend 贷方期末
        """
        resultList = [accountDict[i][index] for i in IDList if i in accountDict]
        return sum(map(float, resultList))

    def findAccountData(self, accountName, isNotNum=False):
        tagList = self.bsObj.findAll("div", {"id": accountName}) 
        if isNotNum:
            tagContentList = [i.get_text() for i in tagList] 
        else:
            tagContentList = [float(i.get_text()) for i in tagList]
        return tagContentList

    def setupDict(self):
        for i in range(self.rows):
            self.accountID.append(self.findAccountData("accountID_{0}".format((i+1)), True)[0])
            self.account.append(self.findAccountData("account_{0}".format((i+1)), True)[0])
            self.opening_debit.append(self.findAccountData("opening_debit_{0}".format((i+1)))[0])
            self.opening_lend.append(self.findAccountData("opening_lend_{0}".format((i+1)))[0])
            self.current_debit.append(sum(self.findAccountData("current_debit_{0}".format((i+1)))))
            self.current_lend.append(sum(self.findAccountData("current_lend_{0}".format((i+1)))))
            self.endtime_debit.append(self.findAccountData("endtime_debit_{0}".format((i+1)))[-1])
            self.endtime_lend.append(self.findAccountData("endtime_lend_{0}".format((i+1)))[-1])
        for i in range(self.rows):
            code = self.accountID[i]
            self.accountDict[code] = [self.account[i], self.opening_debit[i], self.opening_lend[i], self.current_debit[i], self.current_lend[i], self.endtime_debit[i], self.endtime_lend[i]] 

    def setupDatas(self):
        #### 一、短期偿债能力指标 ####

        # 库存现金 + 银行存款 + 交易性金融资产 + 应收账款 + 其他应收款 + 原材料 + 库存商品 + 应交税费 + 生产成本 (debit)
        liquidAsset_list = ['1001', '1002', '1101', '1122', '1221', '1403', '1405', '2221', '5001']
        self.liquidAsset = self.calSumOfIDList(liquidAsset_list, self.accountDict, 5)
        # 库存现金 + 银行存款 + 交易性金融资产 + 应收账款 + 其他应收款 (debit)
        quickAsset_list = ['1001', '1002', '1101', '1122', "1221"]
        self.quickAsset = self.calSumOfIDList(quickAsset_list, self.accountDict, 5)
        # 短期借款 + 应付账款 + 应付职工薪酬 (credit)
        liquidLiability_list = ["2001", "2202", "2211"]
        self.shortTermLiability = self.calSumOfIDList(liquidLiability_list, self.accountDict, 6)

        self.quickRatio = self.quickAsset / self.shortTermLiability
        self.liquidRatio = self.liquidAsset / self.shortTermLiability

        #### 二、长期偿债能力 ####

        # 流动资产 + 固定资产 - 累计折旧 + 研发支出 (debit)
        fixAsset_list = ["1601", "1602", "5301"]
        self.totalAsset = self.liquidAsset + self.calSumOfIDList(fixAsset_list, self.accountDict, 5) - self.calSumOfIDList(fixAsset_list, self.accountDict, 6)
        # 流动负债 + 预计负债 (credit)
        self.totalLiability = self.shortTermLiability + self.calSumOfIDList(["2801"], self.accountDict, 6)

        self.debtAssetRate = self.totalLiability / self.totalAsset
        self.equityMultiplier = 1 / (1 - self.debtAssetRate)

        #### 三、营运能力指标 ####

        #原材料 + 库存商品 + 生产成本 (debit)
        inventory_list = ['1403', '1405', '5001']
        self.inventory_ave = 0.5 * self.calSumOfIDList(inventory_list, self.accountDict, 1) + 0.5 * self.calSumOfIDList(inventory_list, self.accountDict, 5)
        self.inventory_turnover_rate = self.calSumOfIDList(["6401"], self.accountDict, 4) / self.inventory_ave

        self.accountReceivable_ave = 0.5 * self.calSumOfIDList(["1122", "1221"], self.accountDict, 1) + 0.5 * self.calSumOfIDList(["1122", "1221"], self.accountDict, 5)
        self.revenue = self.calSumOfIDList(["6001"], self.accountDict, 3)

        #### 四、盈利能力指标 ####

        self.sale_expense = self.calSumOfIDList(["6601"], self.accountDict, 4)
        self.admin_expense = self.calSumOfIDList(["6602"], self.accountDict, 4)
        self.finan_expense = self.calSumOfIDList(["6603"], self.accountDict, 4)
        self.expense = self.sale_expense + self.admin_expense - self.finan_expense
        self.earn_from_invest = self.calSumOfIDList(["6101", "6111"], self.accountDict, 4)
        self.profit = self.revenue - self.calSumOfIDList(["6401"], self.accountDict, 4) - self.expense - self.earn_from_invest

        #### 五、算分项目 ####

        self.cash = self.calSumOfIDList(["1001", "1002"], self.accountDict, 5)
        beginning_asset = self.calSumOfIDList(liquidAsset_list, self.accountDict, 1) + self.calSumOfIDList(fixAsset_list, self.accountDict, 1) - self.calSumOfIDList(fixAsset_list, self.accountDict, 2)
        self.asset_ave = (beginning_asset + self.totalAsset) / 2
        # 经营现金流入 = 银行存款借方发生额 - 筹资活动现金流入（贷款，实收资本）
        self.operatingCash_in = self.calSumOfIDList(["1002"], self.accountDict, 3) - self.calSumOfIDList(["2001", "4001"], self.accountDict, 4)
        # 经营现金流出 = 银行存款贷方发生额 - 投资活动现金流出 (固定资产)
        self.operatingCash_out = self.calSumOfIDList(["1002"], self.accountDict, 4) - self.calSumOfIDList(["1601"], self.accountDict, 3)

    def printAccount(self):
        for i in range(self.rows):
            print (i, self.accountID[i], self.account[i])

    def printIndex(self):
        print("******************************")
        print("------------------------------")
        print("一、短期偿债能力指标")
        print("  1.流动比率:           {data:0.4f}".format(data=self.liquidRatio))
        print("  2.速动比率:           {data:0.4f}".format(data=self.quickRatio))
        print("------------------------------")
        print("二、短期偿债能力指标")
        print("  1.资产负债率:{data:-15.4f}".format(data=self.debtAssetRate))
        print("  2.权益乘数:  {data:-15.4f}".format(data=self.equityMultiplier))
        print("------------------------------")
        print("三、营运能力指标")
        print("  1.应收帐款周转天数:{data:-10.4f}".format(data=2 * 360 * self.accountReceivable_ave / self.revenue))
        print("  2.存货周转天数:{data:-14.4f}".format(data=2 * 360 / self.inventory_turnover_rate))
        print("  3.资产周转天数:{data:-14.4f}".format(data=360 * self.totalAsset / self.revenue))
        print("------------------------------")
        print("四、盈利能力指标")
        print("  1.销售净利率:{data:-16.4f}".format(data=self.profit / self.revenue))
        print("  2.资产净利率:{data:-16.4f}".format(data=self.profit / self.totalAsset))
        print("  3.权益净利率:{data:-16.4f}".format(data=self.profit / (self.totalAsset - self.totalLiability)))
        print("------------------------------")
        print("******************************")

    def printMark(self, index=0):
        mark = self.mark
        if index == 1:
            mark = self.mark1
        elif index == 2:
            mark = self.mark2
        print("******************************")
        print("-----------------------------------------------")
        print("    算分项目               值              分数")
        print("  1.销售净利率:{data:-15.4f}{mark:-16.2f}".format(data=self.profit / self.revenue, mark=mark[0]))
        print("  2.流动比率:{data:-17.4f}{mark:-16.2f}".format(data=self.liquidRatio, mark=mark[1]))
        print("  3.净现金流:{data:-17.2f}{mark:-16.2f}".format(data=self.cash, mark=mark[2]))
        print("  4.评估收益:{data:-17.4f}{mark:-16.2f}".format(data=(self.totalAsset - self.totalLiability) / 5000000, mark=mark[3]))
        # should be asset_ave actually
        print("  5.总资产报酬率:{data:-14.4f}{mark:-16.2f}".format(data=self.profit / self.totalAsset, mark=mark[4]))
        print("  6.总资产周转率:{data:-14.4f}{mark:-16.2f}".format(data=self.revenue / self.totalAsset, mark=mark[5]))
        print("  7.现金毛利率:{data:-15.4f}{mark:-17.2f}".format(data=(self.operatingCash_in - self.operatingCash_out) / self.operatingCash_in, mark=mark[6]))
        print("  8.存货周转率:{data:-15.4f}{mark:-17.2f}".format(data=self.inventory_turnover_rate, mark=mark[7]))
        print("-----------------------------------------------")
        print("******************************")

    # Methods provided to change the amount
    """
        index = 1 : opening_debit 借方期初
        index = 2 : opening_lend 贷方期初
        index = 3 : current_debit 借方发生额
        index = 4 : current_lend 贷方发生额
        index = 5 : endtime_debit 借方期末
        index = 6 : endtime_lend 贷方期末
    """
    def addAmountToAccount(self, account, amount, index):
        self.accountDict[account][index] = str(float(self.accountDict[account][index]) + amount)
        self.setupDatas()

    def lessAmountToAccout(self, account, amount):
        self.accountDict[account][index] = str(float(self.accountDict[account][index]) - amount)
        self.setupDatas()

if __name__ == '__main__':
    a = WZW(html10+html11, 25)
    # a.printMark()
    a.printIndex()
    # a.printAccount()