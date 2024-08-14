import "../styles/Navbar.css";

const Navbar = () => {
    return (
        <div className="navbar">
            <div className="navbar-container">
                <div className="navbar-links-left">
                    <a href="/">New</a>
                    <a href="/">Upload</a>
                    <a href="/">Share</a>
                </div>
                <div className="navbar-links-right">
                    <div className="v-divider"></div>
                </div>
            </div>
        </div>
    );
};

export default Navbar;
