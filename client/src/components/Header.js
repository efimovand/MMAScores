import React from 'react';
import ufc_logo from '../pic/ufc_logo.png';
import bellator_logo from '../pic/bellator_logo.png';
import pfl_logo from '../pic/pfl_logo.png';


const Header = () => {

    const sub_selected = 1


    return (
        
        <header className='Header' style={{display: 'flex', flexDirection: 'column'}}>
            
            {/* Main*/}
            <div className='main_header' style={{alignContent: 'center', height: '15.5vh', background: '#C55353', padding: '0 40px'}}>
                
                <div className='main_header_container' style={{display: 'flex', flexWrap: 'wrap', justifyContent: 'space-between'}}>
                
                    {/* Logo */}
                    <div className='Logo' style={{height: '10vh', width: '29vw', background: 'grey'}}> 
                        Logo 
                    </div>

                    {/* Menu */}
                    <div className='header_menu' style={{display: 'flex', gap: '30px', alignSelf: 'flex-end'}}> 
                        
                        <div style={{background: '#B83434', height: '5.5vh', width: '11vw'}}>
                            cat 1
                        </div>

                        <div style={{background: '#B83434', height: '5.5vh', width: '11vw'}}>
                            cat 2
                        </div>

                        <div style={{background: '#B83434', height: '5.5vh', width: '11vw'}}>
                            cat 3
                        </div>

                        <div style={{background: '#B83434', height: '5.5vh', width: '11vw'}}>
                            cat 4
                        </div>

                    </div>

                </div>

            </div>

            {/* Sub */}
            <div className='sub_header' style={{display: 'flex', height: '7.2vh', background: '#B83434', padding: '0 30px'}}>
                
                {/* UFC */}
                <div className='sub_category' style={{display: 'flex', flexDirection: 'column', justifyContent: 'space-between', width: '6.5vw', background: 'grey'}}>

                    {/* Logo */}
                    <div className='sub_logo' style={{height: '7vh', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center'}}>
                        <img alt='UFC Logo' src={ufc_logo} style={{height: '26px', width: '26px', scale: '2.5'}} />
                    </div>

                    <div className='sub_selected_line' style={{height: '0.5vh', background: 'white', translate: '0 2px', opacity: sub_selected === 1 ? 1 : 0}}></div>

                </div>

                {/* Bellator */}
                <div className='sub_category' style={{display: 'flex', flexDirection: 'column', justifyContent: 'space-between', width: '6.5vw', background: 'darkgrey'}}>

                    {/* Logo */}
                    <div className='sub_logo' style={{height: '7vh', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center'}}>
                        <img alt='Bellator Logo' src={bellator_logo} style={{height: '45px', width: '45px'}} />
                    </div>

                    <div className='sub_selected_line' style={{height: '0.5vh', background: 'white', translate: '0 2px', opacity: sub_selected === 2 ? 1 : 0}}></div>

                </div>

                {/* PFL */}
                <div className='sub_category' style={{display: 'flex', flexDirection: 'column', justifyContent: 'space-between', width: '6.5vw', background: 'grey'}}>

                    {/* Logo */}
                    <div className='sub_logo' style={{height: '7vh', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center'}}>
                        <img alt='PFL Logo' src={pfl_logo} style={{height: '26px', width: '26px', scale: '2.5'}} />
                    </div>

                    <div className='sub_selected_line' style={{height: '0.5vh', background: 'white', translate: '0 2px', opacity: sub_selected === 3 ? 1 : 0}}></div>

                </div>

            </div>

        </header>

    );

}


export default Header;
