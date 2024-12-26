import React, { useState } from 'react';
import '../Calendar.css';
import { MdExpandMore } from "react-icons/md";


const Calendar = ({ onDateSelect }) => {

    const today = new Date();
    const [currentDate, setCurrentDate] = useState(today);
    const [selectedDate, setSelectedDate] = useState(currentDate);

    // Days of week
    const daysOfWeek = ['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс'];

    // Getting days of month
    const getDaysInMonth = (year, month) => {
        return new Date(year, month + 1, 0).getDate();
    };

    // Start week day (index of the first month's day)
        const getStartDayOfWeek = (year, month) => {
        return new Date(year, month, 1).getDay() || 7; // Monday - 1
    };

    // Month switching
    const handlePrevMonth = () => {
        setCurrentDate(new Date(currentDate.getFullYear(), currentDate.getMonth() - 1, 1));
    };

    const handleNextMonth = () => {
        setCurrentDate(new Date(currentDate.getFullYear(), currentDate.getMonth() + 1, 1));
    };

    // Click on date
    const handleDateClick = (day) => {
        const selected = new Date(currentDate.getFullYear(), currentDate.getMonth(), day);
        setSelectedDate(selected);
        onDateSelect(selected);
    };

    // Today Button
    const handleTodayClick = () => {
        setCurrentDate(today)
        setSelectedDate(today)
    };

    // Data for calendar
    const year = currentDate.getFullYear();
    const month = currentDate.getMonth();
    const daysInMonth = getDaysInMonth(year, month);
    const startDay = getStartDayOfWeek(year, month);


    return (

        <div className="calendar">

            {/* Header */}
            <div className="calendar-header">
                <button onClick={handlePrevMonth}> <MdExpandMore style={{height: '35px', width: '35px', color: '#C55353', rotate: '90deg', marginTop: '3px'}} /> </button>
                <p className='calendar-header-month' style={{fontSize: '14px', fontWeight: 'bold', margin: 0, marginTop: '18px'}}> {currentDate.toLocaleString('en-EN', { month: 'long', year: 'numeric' })} </p>
                <button onClick={handleNextMonth}> <MdExpandMore style={{height: '35px', width: '35px', color: '#C55353', rotate: '-90deg', marginTop: '3px'}} /> </button>
            </div>

            {/* Main */}
            <div className="calendar-days">

                {/* Days Labels */}
                {daysOfWeek.map((day) => (
                    <div key={day} className="calendar-day-name">
                        {day}
                    </div>
                ))}

                {/* Digits */}
                {Array.from({ length: startDay - 1 }).map((_, index) => (
                    <div key={`empty-${index}`} className="calendar-empty"></div>
                ))}
                
                {Array.from({ length: daysInMonth }).map((_, day) => (
                    <button
                        key={day}
                        className={`calendar-day ${
                        selectedDate?.getDate() === day + 1 &&
                        selectedDate?.getMonth() === month &&
                        selectedDate?.getFullYear() === year
                            ? 'selected'
                            : ''
                        }`}
                        onClick={() => handleDateClick(day + 1)}
                    >
                        {day + 1}
                    </button>
                ))}
                
            </div>
            
            {/* Marks Info */}
            <div className='calendar-info' style={{display: 'flex', gap: '9px', alignItems: 'center', height: '40px', background: '#171C1F', padding: '0 18px'}}>
                <div className='calendar-info-mark' style={{height: '5px', width: '9px', border: 'none', borderRadius: '50px', background: '#B83434', marginTop: '-5px'}}></div>
                <p className='calendar-info-text' style={{fontSize: '12px', margin: 0, marginTop: '-5px'}}> Event days </p>
            </div>
            
            {/* Line */}
            <div className='calendar-line' style={{height: '2px', width: '100%', background: '#000000'}}></div>

            {/* Footer */}
            <div className='calendar-footer'>
                <button className='calendar-today-btn' onClick={handleTodayClick}> 
                    <p style={{fontWeight: '14px', color: 'white', fontFamily: 'Geologica', margin: 0}}> Today </p> 
                </button>
            </div>

        </div>
    );
};


export default Calendar;
