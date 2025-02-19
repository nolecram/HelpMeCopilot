variable "project_id" {
  description = "The ID of the project in which to create the LAMP stack resources"
  type        = string
}

variable "region" {
  description = "The Google Cloud region where the LAMP stack resources should be created"
  type        = string
}

variable "zone" {
  description = "The Google Cloud zone where the LAMP stack VM should be created"
  type        = string
}

variable "network" {
  description = "The name of the network to which the LAMP stack VM should be connected"
  type        = string
}
