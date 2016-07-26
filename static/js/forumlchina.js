
function addEvent(oTarget, eventType, listener) {
  if (oTarget.addEventListener) {
    oTarget.addEventListener(eventType, listener, false);
  } else if (oTarget.attachEvent) {
    oTarget['e' + eventType + listener] = listener;
    oTarget[eventType + listener] = function() {
      oTarget['e' + eventType + listener](window.event);
    };
    oTarget.attachEvent('on' + eventType, oTarget[eventType + listener]);
  }
}

function process(ele){
  var lines = ele.innerHTML.split('\n');
  var talks = [];
  var speakers = [];
  var line, speaker;
  var re = /\s*(.*?)(<\/strong>)?<br>/gi;
  for(var i in lines){
    line = lines[i].replace(re, '$1');
    speaker = extract_speaker(line);
    if(speaker){
      talks.push(speaker);
      if(speakers.indexOf(speaker) == -1) speakers.push(speaker.speaker);
    }else{
      talks[talks.length-1].contents.push(line);
    }
  }
  render(ele, speakers, talks);
}

function extract_speaker(line){
  var re = /(<strong>)?(.*?)(\d{2}:\d{2}:\d{2})/gi;
  var result = {contents: []};
  if(line.match(re)){
    line.replace(re, function(){
      result.speaker = arguments[2].trim();
      result.time = arguments[3];
    });
    return result;
  }
  return null;
}

function render(ele, speakers, talks){
  var COLORS = ['#B4402D','#61A0A8','#CC8561','#91C7AE','#BDA29A','#749F83','#69746F'];
  var MAIN_COLOR = '#000';

  ele.innerHTML = talks.map(function(talk){
    var div = document.createElement('DIV');
    var speaker_p = document.createElement('P');
    speaker_p.style.margin = '1em 0 0 0';
    speaker_p.appendChild(document.createTextNode(talk.speaker));

    if(talk.speaker.indexOf('≈Àº””Ó') != -1){
      div.style.fontWeight = 'bold';
      div.style.color = MAIN_COLOR;
      div.style.float = 'right';
      speaker_p.style.float = 'right';
    }else{
      div.style.fontWeight = 'normal';
      div.style.color = COLORS[speakers.indexOf(talk.speaker) % COLORS.length];
      div.style.float = 'left';
      speaker_p.style.float = 'left';
    }

    var span = document.createElement('SPAN');
    span.style.color = '#ccc';
    span.style.paddingLeft = '1em';
    span.appendChild(document.createTextNode(talk.time));

    speaker_p.appendChild(span);
    div.appendChild(speaker_p);

    var split_p = document.createElement('P');
    split_p.style.clear = 'both';
    div.appendChild(split_p);

    talk.contents.map(function(content){
      var content_p = document.createElement('P');
      content_p.style.margin = '0';
      content_p.style.paddingLeft = '2em';
      content_p.style.float = speaker_p.style.float;
      content_p.innerHTML = content;
      div.appendChild(content_p);

      var split_p = document.createElement('P');
      split_p.style.clear = 'both';
      div.appendChild(split_p);
    });

    var split_div = document.createElement('DIV');
    split_div.style.clear = 'both';

    return div.outerHTML + '\n' + split_div.outerHTML;

  }).join('\n');
}


addEvent(window, 'load', function(){
  var eles = document.querySelectorAll("td .p14");
  for(var i in eles){
    if (!eles[i].innerText) continue;
    if (eles[i].innerText.trim() === '') continue;
    process(eles[i]);
  }
});

