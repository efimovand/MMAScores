import React, { useState, useRef, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import '../App.css';
import "@fontsource/geologica";
import { calculateResults } from '../utils/scores';
import { MdExpandMore } from "react-icons/md";
import fightersPics from '../utils/fightersPics';


const MatchPage = ({ backendData }) => {

    // The current Match Data extraction from the Backend Data
    const { date, match } = useParams();
    const event = backendData.find(e => e.date === date);
    const matchData = event?.matches.find(m =>
        `${m.names[0].toLowerCase()}-vs-${m.names[1].toLowerCase()}` === match
    );

    // Match Page
    return (

        <div className='MatchPage' style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>

            <div className='match-page-content' style={{ display: 'flex', flexDirection: 'column', width: '800px', background: '#171C1F', marginTop: '25px', border: 'none', borderRadius: '30px' }}>

                {/* Head */}
                <div className='match-head' style={{ display: 'flex', gap: '20px', margin: '0 20px', marginTop: '20px' }}>

                    {/* Preview (Component) */}
                    <Preview data={matchData} />

                    {/* Stats (Component) */}
                    <Stats data={matchData} />

                </div>

                {/* Judges */}
                <div className='match-judges' style={{ display: 'flex', gap: '20px', margin: '0 20px', marginTop: '30px' }}>

                    {/* Cards (Components) */}
                    {matchData.judges.map((judge, index) => (
                        <JudgeCard
                            key={index}
                            judge={judge.name}
                            names={matchData.names}
                            scores={judge.score}
                        />
                    ))}

                </div>

                {/* Media Scores (Component) */}
                <MediaScores data={matchData} />

            </div>

        </div>

    );

}


// ---------- Preview ----------

// Preview 
const Preview = ({ data }) => {

    return (

        <div className='match-preview' style={{ position: 'relative', width: '460px', height: '170px', border: 'none', borderRadius: '30px' }}>

            {/* Pics + Background */}
            <div className='preview-media' style={{ display: 'flex', justifyContent: 'space-between', height: '100%' }}>

                {/* <-- Side */}
                <div className='preview-side' style={{ alignItems: 'flex-start', borderRadius: '30px 0 0 30px', background: '#0033FF' }}>
                    <img className='preview-img' alt='Fighter 1' src={ fightersPics[data.pics[0]] } style={{ borderRadius: '0 0 0 30px' }} />
                </div>

                {/* --> Side */}
                <div className='preview-side' style={{ alignItems: 'flex-end', borderRadius: '0 30px 30px 0', background: '#C55353' }}>
                    <img className='preview-img' alt='Fighter 2' src={ fightersPics[data.pics[1]] } style={{ borderRadius: '0 0 30px 0' }} />
                </div>

            </div>

            {/* Text */}
            <div className='preview-text'>
                <div className='preview-text-name-1' style={{ height: '60px', textAlign: 'left', marginLeft: '30px' }}> {data.names[0]} </div>
                <div className='preview-text-vs' style={{ height: '50px', textAlign: 'center' }}> vs </div>
                <div className='preview-text-name-2' style={{ height: '60px', textAlign: 'right', marginRight: '30px' }}> {data.names[1]} </div>
            </div>

        </div>

    )

}


// ---------- Stats ----------

// Stats Row
const StatsRow = ({ label, value_1, value_2, isLast = false }) => {

    return (

        <div className='stats-row'>

            {/* Value 1 */}
            <div className='stats-col' style={{ borderRadius: isLast ? '0 0 0 30px' : '0' }}> {value_1} </div>

            {/* Label */}
            <div className='stats-col-label'> {label.toUpperCase()}  </div>

            {/* Value 2 */}
            <div className='stats-col' style={{ borderRadius: isLast ? '0 0 30px 0' : '0' }}>  {value_2} </div>

        </div>
    )

}

// Stats
const Stats = ({ data }) => {

    return (

        <div className='match-stats' style={{ display: 'flex', flexDirection: 'column', width: '280px', height: '170px', border: 'none', borderRadius: '30px', background: '#171C1F' }}>

            {/* Header */}
            <div className='stats-header'> Fighters Stats </div>

            {/* Rows */}
            <div className='stats-rows' style={{ display: 'flex', flexDirection: 'column', gap: '1px' }}>

                {/* Names */}
                <div className='stats-row' style={{ gap: '2px', height: '25px' }}>
                    <div className='stats-col' style={{ width: '139px', fontSize: '14px', fontWeight: 'bold' }}> {data.names[0]} </div>
                    <div className='stats-col' style={{ width: '139px', fontSize: '14px', fontWeight: 'bold' }}> {data.names[1]} </div>
                </div>

                {/* Params */}
                {data.stats.length > 0 ? (  /* If there are some params */
                    <>
                        {data.stats.map((item, index) => (
                            <StatsRow
                                key={index}
                                label={item.param}
                                value_1={item.values[0]}
                                value_2={item.values[1]}
                                isLast={index === data.stats.length - 1}
                            />
                        ))}
                    </>
                ) : (   /* If params' list is empty */
                    <StatsRow label={'Empty'} value_1={''} value_2={''} isLast={true} />
                )}

            </div>

        </div>

    )

}


// ---------- Judge Cards ----------

// Judge Card
const JudgeCard = ({ judge, names, scores }) => {

    const { rounds, sum, winner } = calculateResults(names, scores);
    const resultGradient = winner === names[0] ? 'linear-gradient(180deg, black 0%, #00197F 100%)' : winner === names[1] ? 'linear-gradient(180deg, black 0%, #B83434 100%)' : '#000000'

    return (

        <div className='judge-card' style={{ display: 'flex', flexDirection: 'column', width: '240px', border: 'none', borderRadius: '30px', background: '#171C1F' }}>

            {/* Header */}
            <div className='card-header' style={{ background: '#C55353' }}>
                <p style={{ fontSize: '20px', fontWeight: 'bold', margin: 0 }}> {judge} </p>
            </div>

            {/* Rows */}
            <div className='card-rows' style={{ display: 'flex', flexDirection: 'column', gap: '1px' }}>

                {/* Names */}
                <div className='card-row' style={{ height: '25px' }}>
                    <div className='card-col' style={{ fontWeight: 'bold' }}> {names[0]} </div>
                    <div className='card-col-center' style={{ fontSize: '8px', fontWeight: 'bold' }}> ROUND </div>
                    <div className='card-col' style={{ fontWeight: 'bold' }}> {names[1]} </div>
                </div>

                {/* Rounds */}
                {rounds.map((_, index) => (
                    <div className='card-row' key={index}>
                        <div className='card-col'> {rounds[index][0]} </div>
                        <div className='card-col-center'> {index + 1} </div>
                        <div className='card-col'> {rounds[index][1]} </div>
                    </div>
                ))}

                {/* Total */}
                <div className='card-row' style={{ height: '25px', marginTop: '-0.5px' }}>
                    <div className='card-col' style={{ fontWeight: 'bold', background: resultGradient, borderRadius: '0 0 0 20px' }}> {sum[0]} </div>
                    <div className='card-col-center' style={{ fontSize: '8px', fontWeight: 'bold', background: resultGradient }}> TOTAL </div>
                    <div className='card-col' style={{ fontWeight: 'bold', background: resultGradient, borderRadius: '0 0 20px 0' }}> {sum[1]} </div>
                </div>

            </div>

        </div>

    )

}


// ---------- Media Scores ----------

// Media Card
const MediaCard = ({ names, cite, scores, dark, isLast = false }) => {

    const { rounds, sum, winner } = calculateResults(names, scores);  // Results

    // Expandable rounds
    const [isExpanded, setIsExpanded] = useState(false);
    const cardRef = useRef(null);

    const toggleExpand = () => {
        setIsExpanded((prev) => !prev);
    };

    useEffect(() => {  // Closing rounds after clicking outside

        const handleClickOutside = (event) => {
            if (cardRef.current && !cardRef.current.contains(event.target)) {
                setIsExpanded(false);
            }
        };

        document.addEventListener('mousedown', handleClickOutside);

        return () => {
            document.removeEventListener('mousedown', handleClickOutside);
        };
        
    }, []);


    return (

        <div ref={cardRef} className='media-card' style={{ display: 'flex', flexDirection: 'column' }}>

            {/* Main Row */}
            <div className='media-row' onClick={() => (scores.length > 1 ? toggleExpand() : null)} style={{ position: 'relative', background: dark ? '#000000' : '#0B0E0F', cursor: scores.length > 1 ? 'pointer' : 'default', borderRadius: isLast && !isExpanded ? '0 0 20px 20px' : '0', transition: 'border-radius 0.8s ease' }}>

                {/* More Button */}
                <button className='media-more-btn' style={{ display: scores.length > 1 ? 'inline-block' : 'none' }}>
                    <MdExpandMore style={{ height: '25px', width: '25px', color: '#4A4A4A', margin: 0, transform: isExpanded ? 'rotate(0deg)' : 'rotate(-90deg)', marginTop: '-4.5px', marginLeft: '-8px', transition: 'transform 0.3s ease', }} />
                </button>

                {/* Name + Cite */}
                <div style={{ display: 'flex', flexDirection: 'column', marginLeft: '20px' }}>
                    <div style={{ display: 'inline-block', textAlign: 'center', width: 'max-content' }}>
                        <p className='media-text'> {cite} </p>
                        <p className='media-text'> medianame.com </p>
                    </div>
                </div>

                <div style={{ display: 'flex', alignItems: 'center' }}>

                    {/* Score */}
                    <p className='media-text' style={{ width: '50px', fontWeight: 'bold' }}> {sum[0]} - {sum[1]} </p>

                    {/* Winner */}
                    <p className='media-text' style={{ width: '80px', fontSize: winner.length < 8 ? '14px' : '12px' }}> {winner} </p>

                </div>

            </div>

            {/* Expandable Rounds */}
            <div className='media-expand' style={{ maxHeight: isExpanded && rounds.length < 5 ? '75px' : isExpanded ? '115px' : '0px', padding: isExpanded ? '9px 0' : '0', transition: 'max-height 0.8s ease, padding 0.8s ease', borderRadius: isLast ? '0 0 30px 30px' : '0' }} >

                {/* Rounds */}
                {rounds.map((round, index) => (
                    <div key={index} style={{ display: 'flex', justifyContent: 'space-between', padding: '0 15px' }}>
                        <p style={{ fontSize: '14px', margin: 0, color: '#C55353' }}> Round {index + 1}: </p>
                        <p style={{ fontSize: '14px', margin: 0 }}> {round[0]} - {round[1]} </p>
                    </div>
                ))}

            </div>

        </div>

    )

}

// Media Scores
const MediaScores = ({ data }) => {

    return (

        <div className='match-media-scores' style={{ display: 'flex', flexDirection: 'column', width: '300px', height: 'max-content', margin: '30px 20px 20px 20px', marginTop: '30px', border: 'none', borderRadius: '30px', boxShadow: '0px 4px 4px rgba(0, 0, 0, 0.25)' }}>

            {/* Header */}
            <div className='media-header' style={{ fontSize: '20px', background: '#C55353' }}> Media Scores </div>

            {/* Rows */}
            {data.media.length > 0 ? (  /* If there are some media scores avialable */
                <>
                    {data.media.map((item, index) => (
                        <MediaCard
                            key={index}
                            names={data.names}
                            cite={item.name}
                            scores={item.score}
                            dark={index % 2 === 0}
                            isLast={index === data.media.length - 1}
                        />
                    ))}
                </>
            ) : (   /* If media scores' list is empty */
                <div className='media-row' style={{ fontSize: '14px', justifyContent: 'center' }}> There are no any media scores now </div>
            )}

        </div>

    )

}


export default MatchPage;
