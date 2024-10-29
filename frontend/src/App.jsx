import React from 'react';
import { Tabs } from 'antd';
import LoginForm from './components/LoginForm';
import RegistrationForm from './components/RegistrationForm';

const App = () => {
  return (
    <div style={{ maxWidth: '400px', margin: '50px auto' }}>
      <Tabs defaultActiveKey="1">
        <Tabs.TabPane tab="Login" key="1">
          <LoginForm />
        </Tabs.TabPane>
        <Tabs.TabPane tab="Register" key="2">
          <RegistrationForm />
        </Tabs.TabPane>
      </Tabs>
    </div>
  );
};

export default App;
