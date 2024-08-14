import "../styles/Sidebar.css";

const Sidebar = () => {
    return (
        <div className="sidebar">
            <div className="sidebar-logo">Admin Dashboard</div>
            <div className="divider"></div>
            <ul>
                <li>Add Users</li>
                <li>Delete User</li>
                <li>Update User</li>
                <li>List All Users</li>
            </ul>
        </div>
    );
};

export default Sidebar;
