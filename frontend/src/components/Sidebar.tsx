import "../styles/Sidebar.css";
import { Link } from "react-router-dom";
const Sidebar = () => {
    return (
        <div className="sidebar">
            <div className="sidebar-logo">Dashboard</div>
            <div className="h-divider"></div>
            <ul>
                <li>
                    <Link to="/">Add User</Link>
                </li>
                <li>
                    <Link to="/">Delete User</Link>
                </li>
                <li>
                    <Link to="/">Update User</Link>
                </li>
                <li>
                    <Link to="/">List All Users</Link>
                </li>
            </ul>
        </div>
    );
};

export default Sidebar;
