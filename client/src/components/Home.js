import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import '../App.css';
import "@fontsource/geologica";
import Calendar from './Calendar';
import { calculateResults } from '../utils/scores';
import fightersPics from '../utils/fightersPics';

// For Live Component
import { MdExpandMore } from "react-icons/md";
import rakh_img_live from '../pic_fighters/rakh.png';
import garry_img_live from '../pic_fighters/garry.png';


const Home = ({ backendData }) => {

  // ---------- Pagination ----------
  const [currentPage, setCurrentPage] = useState(1);
  const eventsPerPage = 3; // Number of events per page

  const totalPages = Math.ceil(backendData.length / eventsPerPage);
  const startIndex = (currentPage - 1) * eventsPerPage;
  const currentPageEvents = backendData.slice(startIndex, startIndex + eventsPerPage);

  // Smooth scroll to top after page switching
  useEffect(() => {
    window.scrollTo({
      top: 0,
      left: 0,
      behavior: 'smooth'
    });
  }, [currentPage]);

  // Pagination buttons' handlers
  const handleNextPage = () => {
    if (currentPage < totalPages) setCurrentPage(currentPage + 1);
  };
  const handlePrevPage = () => {
    if (currentPage > 1) setCurrentPage(currentPage - 1);
  };


  // ---------- Live Rounds Data (Examples) ----------
  const liveRoundsData = [
    {
      label: 'Round 1',
      scores: [
        { cite: 'Sherdog.com', score: '10 - 9' },
        { cite: 'mmamania.com', score: '10 - 9' },
        { cite: 'Topology', score: '9 - 10' },
        { cite: 'Topology', score: '9 - 10' },
      ],
    },
    {
      label: 'Round 2',
      scores: [
        { cite: 'Sherdog.com', score: '10 - 9' },
        { cite: 'mmamania.com', score: '10 - 9' },
        { cite: 'Topology', score: '9 - 10' },
      ],
    },
    {
      label: 'Round 3',
      scores: [
        { cite: 'Sherdog.com', score: '10 - 9' },
        { cite: 'mmamania.com', score: '10 - 9' },
      ],
    },
  ];


  // ---------- For Calendar ----------
  const [selectedDate, setSelectedDate] = useState(new Date());
  const handleDateSelect = (date) => {
    setSelectedDate(date);
  };


  // Home Page
  return (

    <div className='Home' style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>

      <div className='home-content' style={{ display: 'flex', gap: '20px', justifyContent: 'center', padding: '25px 20px', width: '1240px' }}>

        {/* ---------- Calendar ---------- */}
        <div className='home-calendar' style={{ width: '350px' }}>
          <Calendar onDateSelect={handleDateSelect} />
        </div>

        {/* ---------- Matches ---------- */}
        <div className='home-matches' style={{ width: '500px' }}>

          {/* Events */}
          {currentPageEvents.map((event, index) => (
            <Event key={index} title={event.title} date={event.date} matches={event.matches} isFirst={index === 0} />
          ))}

          {/* Pagination Buttons */}
          <div className='matches-footer'>
            <button className='matches-pagination-btn' onClick={handlePrevPage} disabled={currentPage === 1}> Prev </button>  {/* Prev */}
            <button className='matches-pagination-btn' onClick={handleNextPage} disabled={currentPage === totalPages}> Next </button>  {/* Next */}
          </div>

        </div>

        {/* ---------- Live ---------- */}
        <div className='home-live' style={{ width: '349px', height: '440px', display: 'flex', flexDirection: 'column', background: '#171C1F', border: 'none', borderRadius: '30px' }}>

          {/* Live Info */}
          <div className='live-info' style={{ marginTop: '10px', justifyItems: 'center' }}>

            {/* Label */}
            <p className='live-label' style={{ fontSize: '16px', fontWeight: 'bold', margin: 0, padding: '0 0 8px 0' }}> LIVE </p>

            {/* Match */}
            <div className='live-match' style={{ display: 'flex', justifyContent: 'center', gap: '55px', width: '333px', height: '85px', background: '#0B0E0F', border: 'none', borderRadius: '15px' }}>

              {/* Fighter 1 */}
              <div className='live-match-fighter'>
                <img className='live-fighter-img' alt='Live Fighter Pic 1' src={rakh_img_live} style={{ height: '50px', width: '50px' }} />
                <p className='live-fighter-name' style={{ fontSize: '10px', margin: 0 }}> Rakhmonov </p>
              </div>

              {/* Time + Round */}
              <div className='live-match-params' style={{ width: '50px', textAlign: 'center', marginTop: '14px' }}>
                <p className='live-match-time' style={{ fontSize: '18px', margin: 0, color: '#C55353' }}> 3:58 </p>
                <p className='live-match-round' style={{ fontSize: '12px', margin: 0, color: '#C55353' }}> Round 1 </p>
              </div>

              {/* Fighter 2 */}
              <div className='live-match-fighter'>
                <img className='live-fighter-img' alt='Live Fighter Pic 2' src={garry_img_live} style={{ height: '50px', width: '50px' }} />
                <p className='live-fighter-name' style={{ fontSize: '10px', margin: 0 }}> Garry </p>
              </div>

            </div>

            {/* Odds */}
            <div className='live-odds' style={{ width: '333px', height: '85px', marginTop: '6px', background: 'linear-gradient(360deg, #171C1F 0%, #0B0E0F 100%)', border: 'none', borderRadius: '15px' }}>
              odds here
            </div>

          </div>

          <div className='live-line' style={{ height: '2px', width: '100%', background: '#000000', marginTop: '10px' }}></div>

          {/* Live Scores */}
          <div className='live-scores' style={{ marginTop: '10px' }}>

            {/* Label */}
            <p className='scores-label' style={{ fontSize: '14px', fontWeight: 'bold', margin: 0, marginLeft: '14px' }}> Live scores: </p>

            {/* Rounds */}
            <div className='scores-rounds' style={{ display: 'flex', marginTop: '15px', textAlign: 'center' }}>

              {/* Round 1 (Component) */}
              <LiveRound data={liveRoundsData[0]} />

              <div className='scores-line' style={{ height: '156px', width: '2px', background: '#707070' }}></div>

              {/* Round 2 (Component) */}
              <LiveRound data={liveRoundsData[1]} />

              <div className='scores-line' style={{ height: '156px', width: '2px', background: '#707070' }}></div>

              {/* Round 3 (Component) */}
              <LiveRound data={liveRoundsData[2]} />

            </div>

          </div>

        </div>

      </div>

    </div>

  );

}


// ---------- Events ----------

// Match
const Match = ({ names, pics, result, judges, dark }) => {

  // Judge Formatted
  const judgeFormatted = judges.map(judge => {
    const { sum } = calculateResults(names, judge.score);
    const lastName = judge.name.split(' ').pop()
    return {
      lastName: lastName,  // Last Name
      scoreSum: `${sum[0]} - ${sum[1]}`,  // Sum Score
      judgeFontSize: lastName.length <= 4 ? '14px' : lastName.length <= 6 ? '12px' : lastName.length <= 8 ? '10px' : '8px', // Judge Font Size
    };
  });

  return (

    <div className='event-match' style={{ display: 'flex', height: '60px', alignItems: 'center', background: '#171C1F' }}>

      {/* Info */}
      <div className='match-info' style={{ display: 'flex', justifyContent: 'space-between', width: '283px', height: '100%', padding: '0 5px', background: dark ? '#0B0E0F' : '#171C1F' }}>

        {/* Pic 1 */}
        <img alt='Fighter Pic 1' src={ fightersPics[pics[0]] } style={{ height: '55px', width: '55px', alignSelf: 'flex-end' }} />

        {/* Text */}
        <div className='match-text' style={{ marginTop: '16px', textAlign: 'center' }}>
          <p className='match-names' style={{ fontSize: '14px', fontWeight: 'bold', margin: 0 }}> {names[0]} vs {names[1]} </p>
          <p className='match-result' style={{ fontSize: '12px', color: '#737373', margin: 0 }}> {result} </p>
        </div>

        {/* Pic 2 */}
        <img alt='Fighter Pic 2' src={ fightersPics[pics[1]] } style={{ height: '55px', width: '55px', alignSelf: 'flex-end' }} />

      </div>

      {/* Judges */}
      {judgeFormatted.map((judge, index) => (

        <div key={index} style={{ display: 'flex', alignItems: 'center', height: '60px' }}>

          {/* Line */}
          <div className='match-line' style={{ width: '2px', height: '42px', background: '#707070' }}></div>

          {/* Judge */}
          <div className='match-judge' style={{ background: dark ? '#0B0E0F' : '#171C1F' }}>

            {/* Score */}
            <p className='judge-score' style={{ fontSize: '12px', fontWeight: 'bold', margin: 0, marginBottom: '13px' }}> {judge.scoreSum} </p>

            {/* Last Name */}
            <div className='judge-name-container'>
              <p className='judge-name' style={{ '--font-size': judge.judgeFontSize }}> {judge.lastName.toUpperCase()} </p>
            </div>

          </div>

        </div>

      ))}

    </div>

  )

}

// Event
const Event = ({ title, date, matches, isFirst }) => {

  return (

    <div className='home-event' style={{ display: 'flex', flexDirection: 'column' }}>

      {/* Header */}
      <div className='event-header' style={{ display: 'flex', flexDirection: 'column', height: '40px', background: '#C55353', textAlign: 'center', justifyContent: 'center', border: 'none', borderRadius: isFirst ? '30px 30px 0 0' : '0' }}>
        <p className='event-header-label' style={{ color: 'white', fontSize: '16px', fontWeight: 'bold' }}> {title} </p>
      </div>

      {/* Matches */}
      {matches.map((match, index) => {

        // Checking is the decision unanimous/split
        const isUnanimous = match.judges.every(judge => {
          const [fighter1, fighter2] = judge.score.reduce(
            ([score1, score2], round) => {
              const [s1, s2] = round.split(' - ').map(Number);
              return [score1 + s1, score2 + s2];
            },
            [0, 0]
          );
          return fighter1 > fighter2; // Возвращаем победителя
        });

        return (
          <Link
            className="home-link"
            key={index}
            to={`/${date}/${`${match.names[0].toLowerCase()}-vs-${match.names[1].toLowerCase()}`}`}
          >
            <Match
              key={index}
              names={match.names}
              pics={match.pics}
              result={isUnanimous ? 'Unanimous' : 'Split'}
              judges={match.judges}
              dark={index % 2 === 0}
            />
          </Link>
        );

      })}

    </div>

  )

}


// ---------- LIVE ----------

// Live Round
const LiveRound = ({ data }) => {

  const scoresToShow = data.scores.slice(0, 3);
  const showMoreButton = data.scores.length >= 4;


  return (

    <div className='live-round' style={{ width: '115px', height: '140px', justifyItems: 'center' }}>

      {/* Label */}
      <p className='live-round-label'> {data.label} </p>

      {/* Scores */}
      {scoresToShow.map((score, index) => (
        <div key={index} className="live-round-score" style={{ background: index % 2 === 0 ? '#0B0E0F' : '#171C1F', borderBottom: index === 1 && data.scores.length === 2 ? '1px solid #0B0E0F' : 'none' }}>
          <p className="score-cite" style={{ fontSize: '10px', margin: 0, marginTop: '4px' }}> {score.cite} </p>
          <p className="score-result" style={{ fontSize: '12px', margin: 0 }}> {score.score} </p>
        </div>
      ))}

      {/* More Button (Optional) */}
      {showMoreButton && (
        <div className='btn-round-more' style={{ height: '25px', width: '25px' }}>
          <MdExpandMore style={{ height: '25px', width: '25px', scale: '1.2', color: '#707070' }} />
        </div>
      )}

    </div>

  );

}


export default Home;
