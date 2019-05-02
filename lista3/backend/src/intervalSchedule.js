
const defineGreaterHour = (date1, date2, labelDate1, labelDate2) => {
    date1Format = new Date()
    date2Format = new Date()
    splitDate1 = date1[labelDate1].split(':')
    splitDate2 = date2[labelDate2].split(':')
    date1Format.setHours(splitDate1[0], splitDate1[1])
    date2Format.setHours(splitDate2[0], splitDate2[1])
    return ((date1Format >= date2Format) ? 1 : 0)
}
module.exports = {
    intervalSchedule(req, res){
        var times = [{"start": '01:25', "final": '06:40'}, {"start": '05:45', "final": '20:45'}, {"start": '07:30', "final": '10:40'}]

        var schedule = []

        times.sort((elm1, elm2) => {
            defineGreaterHour(elm1, elm2, 'final', 'final')
        })


        schedule.push(times[0])
        times.shift()
        
        times.map(item => {
        if(defineGreaterHour(item, schedule[schedule.length - 1], 'start', 'final')){
                schedule.push(item)   
        }
        })

        res.json(schedule);

    }
}


