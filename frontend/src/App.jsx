import { useState } from 'react';
import { MantineProvider, Container, Paper, TextInput, NumberInput, Select, Button, Group, Text, Loader, Box } from '@mantine/core';
import axios from 'axios';
import './App.css';

function App() {
  const [formData, setFormData] = useState({
    age: '',
    gender: '',
    height: '',
    weight: '',
    ap_hi: '',
    ap_lo: '',
    cholesterol: '',
    glucose: '',
    smoking: '',
    alcohol: '',
    physical_activity: ''
  });

  const [prediction, setPrediction] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);

    try {
      const response = await axios.post('http://localhost:5000/predict', formData);
      setPrediction(response.data.prediction);
    } catch (err) {
      setError('An error occurred while making the prediction. Please try again.');
      console.error('Error:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleInputChange = (name, value) => {
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  return (
    <MantineProvider
      theme={{
        colorScheme: 'dark',
        primaryColor: 'blue',
      }}
    >
      <Container size="sm">
        <Paper shadow="md" p="lg" radius="md">
          <Text size="xl" weight={700} align="center" mb="lg">
            Cardiovascular Disease Prediction
          </Text>

          <form onSubmit={handleSubmit}>
            <NumberInput
              label="Age"
              value={formData.age}
              onChange={(value) => handleInputChange('age', value)}
              required
              min={1}
              max={120}
              mb="md"
            />

            <Select
              label="Gender"
              value={formData.gender}
              onChange={(value) => handleInputChange('gender', value)}
              data={[
                { value: '1', label: 'Male' },
                { value: '2', label: 'Female' }
              ]}
              required
              mb="md"
            />

            <Group grow mb="md">
              <NumberInput
                label="Height (cm)"
                value={formData.height}
                onChange={(value) => handleInputChange('height', value)}
                required
                min={100}
                max={250}
              />
              <NumberInput
                label="Weight (kg)"
                value={formData.weight}
                onChange={(value) => handleInputChange('weight', value)}
                required
                min={30}
                max={300}
              />
            </Group>

            <Group grow mb="md">
              <NumberInput
                label="Systolic Blood Pressure"
                value={formData.ap_hi}
                onChange={(value) => handleInputChange('ap_hi', value)}
                required
                min={50}
                max={250}
              />
              <NumberInput
                label="Diastolic Blood Pressure"
                value={formData.ap_lo}
                onChange={(value) => handleInputChange('ap_lo', value)}
                required
                min={30}
                max={150}
              />
            </Group>

            <Select
              label="Cholesterol Level"
              value={formData.cholesterol}
              onChange={(value) => handleInputChange('cholesterol', value)}
              data={[
                { value: '1', label: 'Normal' },
                { value: '2', label: 'Above Normal' },
                { value: '3', label: 'Well Above Normal' }
              ]}
              required
              mb="md"
            />

            <Select
              label="Glucose Level"
              value={formData.glucose}
              onChange={(value) => handleInputChange('glucose', value)}
              data={[
                { value: '1', label: 'Normal' },
                { value: '2', label: 'Above Normal' },
                { value: '3', label: 'Well Above Normal' }
              ]}
              required
              mb="md"
            />

            <Group grow mb="md">
              <Select
                label="Smoking"
                value={formData.smoking}
                onChange={(value) => handleInputChange('smoking', value)}
                data={[
                  { value: '0', label: 'No' },
                  { value: '1', label: 'Yes' }
                ]}
                required
              />
              <Select
                label="Alcohol Consumption"
                value={formData.alcohol}
                onChange={(value) => handleInputChange('alcohol', value)}
                data={[
                  { value: '0', label: 'No' },
                  { value: '1', label: 'Yes' }
                ]}
                required
              />
            </Group>

            <Select
              label="Physical Activity"
              value={formData.physical_activity}
              onChange={(value) => handleInputChange('physical_activity', value)}
              data={[
                { value: '0', label: 'Inactive' },
                { value: '1', label: 'Active' }
              ]}
              required
              mb="xl"
            />

            <Button
              type="submit"
              fullWidth
              loading={loading}
              disabled={loading}
            >
              Predict
            </Button>
          </form>

          {error && (
            <Text color="red" size="sm" mt="md" align="center">
              {error}
            </Text>
          )}

          {prediction !== null && !error && (
            <Box mt="xl" p="md" bg={prediction === 1 ? 'red.9' : 'green.9'} style={{ borderRadius: '8px' }}>
              <Text align="center" weight={700} color="white">
                {prediction === 1
                  ? 'HIGH RISK of Cardiovascular Disease Detected'
                  : 'Low risk of Cardiovascular Disease'
                }
              </Text>
            </Box>

          )}
        </Paper>
      </Container>
    </MantineProvider>
  );
}

export default App;