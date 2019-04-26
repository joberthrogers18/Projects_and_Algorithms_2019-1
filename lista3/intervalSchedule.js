
const defineGreaterHour = (date1, date2) => {
    date1Format = new Date()
    date2Format = new Date()
    splitDate1 = date1.final.split(':')
    splitDate2 = date2.final.split(':')
    console.log('passou')
    date1Format.setHours(splitDate1[0], splitDate1[1])
    date2Format.setHours(splitDate2[0], splitDate2[1])
    console.log(date1Format)
    console.log(date2Format)
    return ((date1Format > date2Format) ? 1 : -1)
}

const intervalSchedule = () => {
    var times = [{"start": '05:00', "final": '15:03'}, {"start": '10:30', "final": '14:45'}, {"start": '02:30', "final": '06:40'}]

    var schedule = []

    if(schedule == []){
        schedule.push(times[0])
        times.pop(0)
    }

    times.sort(defineGreaterHour)

    console.log(times)

}

intervalSchedule()

