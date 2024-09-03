import React from "react";
import { useFetchData } from "../hooks/useFetchData";
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from "chart.js";
import { Pie } from "react-chartjs-2";

ChartJS.register(ArcElement, Tooltip, Legend);

type ChartProps = {
    url: string;
};

interface MemoryData {
    available_memory: string;
    total_memory: string;
    used_memory: string;
    usage_percentage: string;
    response_code: number;
}

const DonutChartMemory: React.FC<ChartProps> = ({ url }) => {
    const { data, error, loading } = useFetchData<MemoryData>(url);

    const chartData = React.useMemo(() => {
        if (!data) return null;

        const usedMemory = parseFloat(data.used_memory);
        const availableMemory = parseFloat(data.available_memory);

        return {
            labels: ["Used Memory", "Available Memory"],
            datasets: [
                {
                    label: "Memory Usage",
                    data: [usedMemory, availableMemory],
                    backgroundColor: [
                        "rgba(255, 99, 132, 0.8)",
                        "rgba(54, 162, 235, 0.8)",
                    ],
                    borderColor: [
                        "rgba(255, 99, 132, 1)",
                        "rgba(54, 162, 235, 1)",
                    ],
                    borderWidth: 1,
                },
            ],
        };
    }, [data]);
    const options = {
        responsive: true,
        maintainAspectRation: false,
        cutout: "70%",
        radius: "70%",
    };
    return (
        <div
            className="test-container"
            style={{ width: "305px", height: "305px" }}
        >
            {loading && <h1>Loading</h1>}
            {error && <h1>{error}</h1>}
            {chartData && <Pie data={chartData} options={options} />}
        </div>
    );
};

export default DonutChartMemory;
