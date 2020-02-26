# Fill Feedback Forms Automagically

Utilise these Functions to fill the well-known yet annoying feedback forms.

### Instructions

- Log in
- Open browser's built-in developer console by following any of the step:
  - Hit `F12` and open console
  - Press `Ctrl+Shift+j`
- Once the form appears, choose subject
- Copy required functions given below
- Paste in the open console and hit `Enter`
- Call any function you like and hit `Enter`
- Repeat the above steps for all subjects

### To Give Good Rating In All Criterion

```javascript
function markGood(){
  for (i = 0; i < 6; i++)
  {
    document.getElementById("txtComments").value="NO COMMENTS";
    $("input[id='ctl02_gvFeedback_rbtnQuestion_"+i+"_0_"+i+"']").click()
    $("input[id='btnSubmit']").click()
  }
}
```

### To Give Neutral Rating In All Criterion

```javascript
function markNeutral(){
  for (i = 0; i < 6; i++)
  {
    document.getElementById("txtComments").value="NO COMMENTS";
    $("input[id='ctl02_gvFeedback_rbtnQuestion_"+i+"_1_"+i+"']").click()
    $("input[id='btnSubmit']").click()
  }
}
```

### To Give Bad Rating In All Criterion

```javascript
function markBad(){
  for (i = 0; i < 6; i++)
  {
    document.getElementById("txtComments").value="NO COMMENTS";
    $("input[id='ctl02_gvFeedback_rbtnQuestion_"+i+"_2_"+i+"']").click()
    $("input[id='btnSubmit']").click()
  }
}
```
