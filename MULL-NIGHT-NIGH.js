const toggleBtn = document.getElementById('toggleBtn');
const status = document.getElementById('status');
let isNight = false;
let colorScheme = 'default';
let soundEnabled = true;

const themes = {
  default: {
    day: { bg: '#111', text: '#fff', accent: '#6ec5ff' },
    night: { bg: '#020617', text: '#fff', accent: '#ffa500' }
  },
  cyberpunk: {
    day: { bg: '#1a1a2e', text: '#00ff00', accent: '#ff006e' },
    night: { bg: '#0f0f23', text: '#00ff00', accent: '#ff006e' }
  },
  ocean: {
    day: { bg: '#e0f7ff', text: '#003d5c', accent: '#006ba6' },
    night: { bg: '#001f3f', text: '#00d9ff', accent: '#0099cc' }
  },
  forest: {
    day: { bg: '#c8e6c9', text: '#1b5e20', accent: '#2e7d32' },
    night: { bg: '#1b5e20', text: '#c8e6c9', accent: '#81c784' }
  }
};

function applyTheme() {
  const theme = themes[colorScheme][isNight ? 'night' : 'day'];
  document.body.style.background = theme.bg;
  document.body.style.color = theme.text;
  document.documentElement.style.setProperty('--accent-color', theme.accent);
  
  if (soundEnabled) playTransitionSound();
}

function playTransitionSound() {
  // Simulate sound with visual feedback
  const audioContext = new (window.AudioContext || window.webkitAudioContext)();
  const oscillator = audioContext.createOscillator();
  const gainNode = audioContext.createGain();
  
  oscillator.connect(gainNode);
  gainNode.connect(audioContext.destination);
  
  oscillator.frequency.value = isNight ? 150 : 400;
  oscillator.type = 'sine';
  
  gainNode.gain.setValueAtTime(0.1, audioContext.currentTime);
  gainNode.gain.exponentialRampToValueAtTime(0.01, audioContext.currentTime + 0.3);
  
  oscillator.start(audioContext.currentTime);
  oscillator.stop(audioContext.currentTime + 0.3);
}

function toggleMode() {
  isNight = !isNight;
  toggleBtn.textContent = isNight ? 'Switch to Day ☀️' : 'Switch to Night 🌙';
  status.textContent = `Current mode: ${isNight ? 'Night' : 'Day'} | Theme: ${colorScheme.toUpperCase()}`;
  applyTheme();
}

function changeTheme(theme) {
  colorScheme = theme;
  applyTheme();
  status.textContent = `Current mode: ${isNight ? 'Night' : 'Day'} | Theme: ${colorScheme.toUpperCase()}`;
}

function toggleSound() {
  soundEnabled = !soundEnabled;
  updateControlPanel();
}

function updateControlPanel() {
  controlStatus.textContent = `Sound: ${soundEnabled ? '🔊 ON' : '🔇 OFF'}`;
}

toggleBtn.addEventListener('click', toggleMode);

// Create theme selector
const themeDiv = document.createElement('div');
themeDiv.style.cssText = 'margin: 15px; display: flex; gap: 10px; flex-wrap: wrap;';
Object.keys(themes).forEach(theme => {
  const btn = document.createElement('button');
  btn.textContent = theme.charAt(0).toUpperCase() + theme.slice(1);
  btn.style.cssText = 'padding: 8px 16px; cursor: pointer; background: #333; color: #fff; border: 1px solid #666; border-radius: 4px;';
  btn.addEventListener('click', () => changeTheme(theme));
  themeDiv.appendChild(btn);
});
document.body.insertBefore(themeDiv, status.nextElementSibling);

// Create sound toggle
const soundDiv = document.createElement('div');
soundDiv.style.cssText = 'margin: 15px;';
const soundBtn = document.createElement('button');
soundBtn.textContent = 'Toggle Sound';
soundBtn.style.cssText = 'padding: 8px 16px; cursor: pointer; background: #333; color: #fff; border: 1px solid #666; border-radius: 4px;';
soundBtn.addEventListener('click', toggleSound);
const controlStatus = document.createElement('span');
controlStatus.style.cssText = 'margin-left: 15px;';
soundDiv.appendChild(soundBtn);
soundDiv.appendChild(controlStatus);
document.body.insertBefore(soundDiv, themeDiv.nextElementSibling);

// Initialize
applyTheme();
updateControlPanel();
