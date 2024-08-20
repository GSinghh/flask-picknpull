interface Data {
    [key: string]: string;
}

interface DropdownData {
    data: Data;
}

const Dropdown: React.FC<DropdownData> = ({ data }) => {
    const options = Object.entries(data).map(([value, label]) => ({
        value,
        label,
    }));
    return (
        <select>
            {options.map((option) => (
                <option key={option.value} value={option.value}>
                    {option.label}
                </option>
            ))}
        </select>
    );
};
export default Dropdown;
