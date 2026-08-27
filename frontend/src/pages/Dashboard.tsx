import { useEffect, useState } from "react";
import api from "../services/api";
import RouterCard from "../components/RouterCard";
import SystemCard from "../components/SystemCard";
import NetworkCard from "../components/NetworkCard";
import WirelessCard from "../components/WirelessCard";
import DhcpCard from "../components/DhcpCard";

// interface DashboardProps{
//   router: Record<string,any>
//   system: Record<string,any>
//   network: Record<string,any>
//   wireless: Record<string,any>
//   process: Record<string,any>
// }

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

  if (!dashboard) {
    return <div>dashboard loading...</div>;
  }

  return (
    <div className="dashboard">
      <h1>Network Dashboard</h1>
      <div className="dashboard-grid">
        <RouterCard router={dashboard.router} />
        <SystemCard system={dashboard.system} />
        <NetworkCard network={dashboard.network} />
        <WirelessCard wireless={dashboard.wireless}/>
        <DhcpCard dhcp={dashboard.dhcp}/>
      </div>
    </div>
  );
}
