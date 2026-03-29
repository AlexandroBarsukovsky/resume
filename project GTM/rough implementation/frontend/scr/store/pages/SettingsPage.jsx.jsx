import React, { useState } from 'react';
import SliderSetting from '../components/Settings/SliderSetting';

export default function SettingsPage() {
  const [settings, setSettings] = useState({
    accountScoreThreshold: 0.7,
    healthScoreThreshold: 0.5,
    forecastHorizonDays: 30,
  });

  const handleChange = (key, value) => {
    setSettings(prev => ({ ...prev, [key]: value }));
    // здесь можно отправить изменения на сервер
  };

  return (
    <div className="max-w-2xl mx-auto space-y-6">
      <h1 className="text-2xl font-bold">Настройки системы</h1>
      <SliderSetting
        label="Порог Account Score для автоматической квалификации"
        value={settings.accountScoreThreshold}
        min={0}
        max={1}
        step={0.05}
        onChange={(v) => handleChange('accountScoreThreshold', v)}
      />
      <SliderSetting
        label="Порог Health Score для красной зоны"
        value={settings.healthScoreThreshold}
        min={0}
        max={1}
        step={0.05}
        onChange={(v) => handleChange('healthScoreThreshold', v)}
      />
      <SliderSetting
        label="Горизонт прогноза (дни)"
        value={settings.forecastHorizonDays}
        min={7}
        max={90}
        step={7}
        onChange={(v) => handleChange('forecastHorizonDays', v)}
      />
    </div>
  );
}