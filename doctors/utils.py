from datetime import datetime, timedelta

def get_daily_slots(doctor, appointment_date):

    day_name = appointment_date.strftime("%A") 
    schedules = doctor.schedules.filter(day_of_week=day_name, is_active=True)
    
    slots_list = []

    for schedule in schedules:
        start = datetime.combine(appointment_date, schedule.start_time)
        end = datetime.combine(appointment_date, schedule.end_time)
        slot_duration = timedelta(minutes=schedule.slot_duration)

        current_slot = start
        while current_slot + slot_duration <= end:
            slot_time = current_slot.time()

            is_booked = doctor.appointments.filter(
                appointment_date=appointment_date,
                start_time=slot_time,
                status='scheduled'
            ).exists()

            slots_list.append({
                "slot": slot_time,
                "status": "booked" if is_booked else "available"
            })

            current_slot += slot_duration

    return slots_list