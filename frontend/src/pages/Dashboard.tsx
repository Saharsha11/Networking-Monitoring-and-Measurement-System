import { useEffect, useState } from "react";
import api from "../services/api";

export function Dashboard() {
  const [dashboard, setDashboard] = useState<any>(null);

  useEffect(() => {
    const fetchBoard = async () => {
      try {
        const response = await api.get("router/dashboard/");
        console.log(response.data);
        setDashboard(response.data);
      } catch (error) {
        console.log("Error: ", error);
      }
    };
    fetchBoard();
  }, []);

  if(!dashboard){
    return <div>dashboard loading...</div>;
  }

  return(
      <div>
            <h1>Network Dashboard</h1>

            <h2>{dashboard.router.hostname}</h2>
            <p>{dashboard.router.model}</p>

            <pre>
                {JSON.stringify(dashboard, null, 2)}
            </pre>
        </div>
  )
}
