import { useRef } from 'react';
import { Link } from 'react-router-dom'; // Link is used to prevent the page from reloading when the user clicks on a link

const Header = () => {
    const navRef = useRef(null);

    const toggleNav = () => {
        navRef.current.classList.toggle('responsive-nav');
    }

    const closeNav = () => {
        navRef.current.classList.remove('responsive-nav');
    }
    return (
        <div className="header">
            <h1><Link to="/">Personality Predictor</Link></h1>
            <nav ref={navRef} className="navbar">
                <Link to="/" onClick={closeNav}>Home</Link>
                <Link to="/about" onClick={closeNav} style={
                    {
                        // // CSS in JS
                        // color: "white",
                        // backgroundColor: "#f1356d",
                        // borderRadius: "8px"
                    }
                }>About</Link>
                <button className='nav-btn close-btn' onClick={toggleNav}>
                    <img className='btn-icon' src='close.svg' alt='close'></img>
                </button>
            </nav>
            <button className='nav-btn' onClick={toggleNav}>
                <img className='btn-icon' src='hamburger-menu.svg' alt='menu'></img>
            </button>
        </div>
    );
}
 
export default Header;