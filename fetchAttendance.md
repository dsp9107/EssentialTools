# Generate JSON Object For Attendance Data Automagically

Utilise these Functions to fetch attendance data and store the same in JSON format.

### Instructions

- Log in
- Navigate to attendance page
- Open browser's built-in developer console by following any of the step:
  - Hit `F12` and open console
  - Press `Ctrl+Shift+j`
- Copy required functions given below
- Paste in the open console and hit `Enter`
- Call any function you like and hit `Enter`
- Use the data to do amazing things

### To Fetch And Return Headers And Data

```javascript
function copy() {
    data = [];
    keys = [];
    $("tr")
        .find("th")
        .each(function() {
            keys.push($(this).text());
        });
    $("tr").each(function() {
        temp = [];
        $(this)
            .find("td")
            .each(function() {
                temp.push($(this).text());
            });
        if (temp.length > 0) {
            data.push(temp);
        }
    });
    return { keys, data };
}
```

### To Generate JSON Object For Provided Keys And Corresponding Data

```javascript
function generate({ keys, data }) {
    x = {};
    keys.forEach(key => {
        x[key] = "";
    });
    actual = [];
    for (i = 0; i < data.length; i++) {
        temp = [];
        for (j = 0; j < data.length; j++) {
            temp.push({
                [keys[j]]: data[i][j]
            });
        }
        actual.push(temp);
    }
    return actual;
}
```

### Recommended Usage

```javascript
let myAttendanceData = generate(copy());
```
