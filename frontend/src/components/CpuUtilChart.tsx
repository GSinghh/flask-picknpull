import React from "react";
import { useFetchData } from "../hooks/useFetchData";
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from "chart.js";
import { Pie } from "react-chartjs-2";

ChartJS.register(ArcElement, Tooltip, Legend);

type ChartProps = {
    url: string;
};

interface CPUData {
    cpu_usage: number;
    cpu_freq: number[];
    avg_load: number[];
    response_code: number;
}

const CpuUtilChart: React.FC<ChartProps> = ({ url }) => {
    const { data, error, loading } = useFetchData<CPUData>(url);

    const chartData = React.useMemo(() => {
        if (!data) return null;

        const cpu_usage = data.cpu_usage;
        const idle_usage = 100 - cpu_usage; // Calculate idle usage

        return {
            labels: ["CPU Usage", "Idle"],
            datasets: [
                {
                    data: [cpu_usage, idle_usage],
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
        maintainAspectRatio: false,
        radius: "75%",
    };

    return (
        <div
            className="cpu-chart-container"
            style={{ width: "100%", maxWidth: "600px" }}
        >
            {loading && <h1>Loading</h1>}
            {error && <h1>{error}</h1>}
            {chartData && (
                <div style={{ height: "300px" }}>
                    <Pie data={chartData} options={options} />
                </div>
            )}
        </div>
    );
};

export default CpuUtilChart;
