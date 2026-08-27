interface SystemCardProps {
  system: {
    uptime: number;
    load: number[];
    memory: {
      total: number;
      free: number;
      available: number;
    };
  };
}

function formatBytes(bytes: number) {
  if (bytes === 0) return "0 B";

  const units = ["B", "KB", "MB", "GB"];
  const index = Math.floor(Math.log(bytes) / Math.log(1024));

  return `${(bytes / Math.pow(1024, index)).toFixed(1)} ${units[index]}`;
}

function formatUptime(seconds: number) {
  const days = Math.floor(seconds / 86400);
  const hours = Math.floor((seconds % 86400) / 3600);
  const minutes = Math.floor((seconds % 3600) / 60);

  return `${days}d ${hours}h ${minutes}m`;
}

function SystemCard({ system }: SystemCardProps) {
  const memoryUsed = system.memory.total - system.memory.available;

  const memoryPercentage = (memoryUsed / system.memory.total) * 100;

  return (
    <div className="dashboard-card">
      <h2>System Status</h2>

      <div className="metric-grid">
        {/* CPU Load */}
        <div className="metric">
          <span className="metric-label">CPU Load</span>

          <strong className="metric-value">{system.load[0]}</strong>
        </div>

        {/* Memory */}
        <div className="metric">
          <span className="metric-label">Memory</span>

          <strong className="metric-value">
            {memoryPercentage.toFixed(1)}%
          </strong>

          <div className="progress-bar">
            <div
              className="progress-fill"
              style={{
                width: `${memoryPercentage}%`,
              }}
            />
          </div>

          <small>
            {formatBytes(memoryUsed)} / {formatBytes(system.memory.total)}
          </small>
        </div>

        {/* Uptime */}
        {/* Uptime */}
        <div className="metric uptime-metric">
          <span className="metric-label">Uptime</span>

          <strong className="metric-value">
            {formatUptime(system.uptime)}
          </strong>
        </div>
      </div>
    </div>
  );
}

export default SystemCard;
