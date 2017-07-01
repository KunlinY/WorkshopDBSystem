function st(){
    setTimeout(ta,1000);
}  
function ta(){
var theTable = document.getElementById("tablelsw");     
var totalPage = document.getElementById("spanTotalPage");     
var pageNum = document.getElementById("spanPageNum");     
    
var spanPre = document.getElementById("spanPre");     
var spanNext = document.getElementById("spanNext");     
var spanFirst = document.getElementById("spanFirst");     
var spanLast = document.getElementById("spanLast");     
    
var totalPaget = document.getElementById("spanTotalPaget");     
var pageNumt = document.getElementById("spanPageNumt");     
    
var spanPret = document.getElementById("spanPret");     
var spanNextt = document.getElementById("spanNextt");     
var spanFirstt = document.getElementById("spanFirstt");     
var spanLastt = document.getElementById("spanLastt");     
    
var numberRowsInTable = theTable.rows.length;     
var pageSize = 4;     
var page = 1;     
    
//下一页     
      for ( var i = 0; i<pageSize; i++ ){     
        theTable.parentNode.style.display = '';     
    }     
    
//上一页 

    
function hideTable(){     
    for ( var i = 0; i<numberRowsInTable; i++ ){     
        theTable.rows[i].style.display = 'none';     
    }     
} 

function preTable(){     
    
    hideTable();     
         
    page--;     
         
    currentRow = pageSize * page;     
    maxRow = currentRow - pageSize;     
    if ( currentRow > numberRowsInTable ) currentRow = numberRowsInTable;     
    for ( var i = maxRow; i< currentRow; i++ ){     
        theTable.rows[i].style.display = '';     
    }     
         
         
    if ( maxRow == 0 ){ preText(); firstText(); }     
    showPage();     
    nextLink();     
    lastLink();     
}     
    
    function nextTable(){     
    
    hideTable();     
         
    currentRow = pageSize * page;     
    maxRow = currentRow + pageSize;     
    if ( maxRow > numberRowsInTable ) maxRow = numberRowsInTable;     
    for ( var i = currentRow; i< maxRow; i++ ){     
        theTable.rows[i].style.display = '';     
    }     
    page++;     
         
    if ( maxRow == numberRowsInTable ) { nextText(); lastText(); }     
    showPage();     
    preLink();     
    firstLink();     
}   
//第一页     
function firstTable(){     
    hideTable();     
    page = 1;     
    for ( var i = 0; i<pageSize; i++ ){     
        theTable.rows[i].style.display = '';     
    }     
    showPage();     
         
    preText();     
    nextLink();     
    lastLink();     
}     
    
//最后一页     
function lastTable(){     
    hideTable();     
    page = pageCount();     
    currentRow = pageSize * (page - 1);     
    for ( var i = currentRow; i<numberRowsInTable; i++ ){     
        theTable.rows[i].style.display = '';     
    }     
    showPage();     
         
    preLink();     
    nextText();     
    firstLink();     
}         
    
function showPage(){     
    pageNum.innerHTML = page;     
    pageNumt.innerHTML = page;     
}     
    
//总共页数     
function pageCount(){     
    var count = 0;     
    if ( numberRowsInTable%pageSize != 0 ) count = 1;      
    return parseInt(numberRowsInTable/pageSize) + count;     
}     
    
//显示链接     
function preLink(){ spanPre.innerHTML = "<a onclick='<a href='javascript:preTable();'>' href='#'>上一页</a>"; spanPret.innerHTML = "<a href='javascript:preTable();'>上一页</a>";}     
function preText(){ spanPre.innerHTML = "上一页"; spanPret.innerHTML = "上一页"; }     
    
function nextLink(){ spanNext.innerHTML = "<a href='javascript:nextTable();'>下一页</a>"; spanNextt.innerHTML = "<a href='javascript:nextTable();'>下一页</a>";}     
function nextText(){ spanNext.innerHTML = "下一页"; spanNextt.innerHTML = "下一页";}     
    
function firstLink(){ spanFirst.innerHTML = "<a href='javascript:firstTable();'>第一页</a>"; spanFirstt.innerHTML = "<a href='javascript:firstTable();'>第一页</a>";}     
function firstText(){ spanFirst.innerHTML = "第一页"; spanFirstt.innerHTML = "第一页";}     
    
function lastLink(){ spanLast.innerHTML = "<a href='javascript:lastTable();'>最后一页</a>"; spanLastt.innerHTML = "<a href='javascript:lastTable();'>最后一页</a>";}     
function lastText(){ spanLast.innerHTML = "最后一页"; spanLastt.innerHTML = "最后一页";}     
    
//隐藏表格     
function hide(){     
    for ( var i = pageSize; i<numberRowsInTable; i++ ){     
        theTable.rows[i].style.display = 'none';     
    }     
         
    totalPage.innerHTML = pageCount();     
    pageNum.innerHTML = '1';     
         
    totalPaget.innerHTML = pageCount();     
    pageNumt.innerHTML = '1';     
         
    nextLink();     
    lastLink();     
}     
    
hide();
} 